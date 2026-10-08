import json, math, re, base64, html, copy
from pathlib import Path
import xml.etree.ElementTree as ET
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from PIL import Image
P=Path(__file__).resolve().parent
C=json.loads((P/'current.json').read_text()); raw=json.loads((P/'old.xml.json').read_text())
extra={}
for e in json.loads((P/'old-nested-raw.json').read_text()):
 if e['status']=='fulfilled':
  for b in e['value']['result'].get('content',[]):
   if b.get('text','').startswith('<'):extra[e['value']['id']]=ET.fromstring(b['text'])
def parse(el):
 d=dict(el.attrib);d['type']=el.tag;d['visible']=d.pop('hidden','false')!='true'
 for k in ['x','y','width','height']:d[k]=float(d.get(k,0))
 d['children']=[parse(c) for c in el]
 if not d['children'] and d['id'] in extra:d['children']=[parse(c) for c in extra[d['id']]]
 return d
O={k:parse(ET.fromstring(v)) for k,v in raw.items()}
ids=list(C);featured=ids[:27];meta=ids[27:]
def fmt(v):
 if v is None:return '-'
 if isinstance(v,str):return v
 if abs(v)<.00005:v=0
 return f'{v:.2f}'.rstrip('0').rstrip('.')
def dims(n):return fmt(n['width'])+' × '+fmt(n['height'])
def flatten(n,path='',visible=True,xy=(0,0),root=True):
 path=(path+' / ' if path else '')+n['name'];v=visible and n.get('visible',True)
 ax=xy[0]+(0 if root else n.get('x',0));ay=xy[1]+(0 if root else n.get('y',0))
 yield n,path,v,ax,ay
 for c in n.get('children',[]):yield from flatten(c,path,v,(ax,ay),False)
def find(n,name):return next((x for x,_,_,_,_ in flatten(n)if x['name']==name),None)
def changes(id):
 old={n['id']:(n,path,v,ax,ay)for n,path,v,ax,ay in flatten(O[id])};out=[]
 for n,path,v,ax,ay in flatten(C[id]):
  if n['id'] not in old:continue
  a,_,av,aax,aay=old[n['id']]
  for k in ['width','height','x','y']:
   if n['id']==id and k in ['x','y']:continue
   if abs(n.get(k,0)-a.get(k,0))>.01:out.append([path.split(' / ',1)[-1],n['id'],k,fmt(a[k]),fmt(n[k]),fmt(n[k]-a[k]),'видим' if v else 'скрыт'])
  if av!=v:out.append([path,n['id'],'visible',str(av),str(v),'-','видимость'])
 return out
allchanges={id:changes(id)for id in ids};(P/'geometry-diff.json').write_text(json.dumps(allchanges,ensure_ascii=False,indent=2))
def title(n):return n['name'].replace('🔴','').replace('Device=','').replace('Content=','').replace('Trailer=False','без трейлера').replace('Trailer=True','трейлер')
# Annotation rectangles use measured geometry, keeping original renders intact.
COLORS={'changed':'#FFB020','removed':'#FF5277','added':'#20D6A4'}
def marks(id, side):
 a,b=O[id],C[id]
 old={n['id']:(n,path,v,x,y) for n,path,v,x,y in flatten(a)}
 new={n['id']:(n,path,v,x,y) for n,path,v,x,y in flatten(b)}
 source,other=(old,new) if side=='old' else (new,old)
 out=[]
 for nid,(n,path,v,x,y) in source.items():
  if not v:continue
  if nid in other:
   q,_,qv,_,_=other[nid]
   changed=any(abs(n.get(k,0)-q.get(k,0))>.01 for k in (['width','height'] if nid==id else ['x','y','width','height']))
   if changed:out.append((n,x,y,'changed'))
  else:
   # Only mark confirmed structural changes under an expanded matched parent.
   parent=next((z for z,_,_,_,_ in flatten(a if side=='old' else b) if any(c['id']==nid for c in z.get('children',[]))),None)
   if parent and parent['id'] in other and other[parent['id']][0].get('children'):
    out.append((n,x,y,'removed' if side=='old' else 'added'))
 # Suppress dense descendants when a marked immediate visual container already explains them.
 selected=[]
 preferred={'labelGroup','Spasibo Badge','Logo Title Img','Meta - Text','Meta - Text Group','Text Box','Meta media','PageIndicator','Text Name'}
 for n,x,y,kind in out:
  if n['id']==id or n['name'] in preferred or (n['type'] in ['TEXT','text'] and not any(z['name'] in preferred and zx<=x and zy<=y and zx+z['width']>=x+n['width']-.1 and zy+z['height']>=y+n['height']-.1 for z,zx,zy,zk in out)):
   selected.append((n,x,y,kind))
 return selected

def pdf_marks(id,side,origin_x,top,scale):
 for n,x,y,kind in marks(id,side):
  cv.saveState();cv.setStrokeColor(HexColor(COLORS[kind]));cv.setLineWidth(1.3)
  if kind=='removed':cv.setDash(3,2)
  cv.rect(origin_x+x*scale,top-(y+n['height'])*scale,n['width']*scale,n['height']*scale,stroke=1,fill=0)
  cv.restoreState()

def overlay_svg(id,side):
 root=O[id] if side=='old' else C[id]
 out=f'<svg class="marks" viewBox="0 0 {root["width"]} {root["height"]}" style="position:absolute;inset:0;width:100%;height:100%;overflow:visible;pointer-events:none">'
 for n,x,y,kind in marks(id,side):
  dash='stroke-dasharray="5 3"' if kind=='removed' else ''
  out+=f'<rect x="{x}" y="{y}" width="{n["width"]}" height="{n["height"]}" fill="none" stroke="{COLORS[kind]}" stroke-width="2" vector-effect="non-scaling-stroke" {dash}><title>{html.escape(n["name"])}: {kind}</title></rect>'
 return out+'</svg>'

def differs(a,b):return str(a).replace('*','').strip()!=str(b).replace('*','').strip()

summary=[
('Телефон: квадратный Featured','Все 9 вариантов: 360 × 391 → 360 × 360. Высота −31 (−7,93%); W/H: 0,9207 → 1. Tablet Portrait остаётся 640 × 363, Landscape — 1024 × 362.'),
('Лейблы отделены от Meta','labelGroup исчезает из соответствующих базовых Meta и появляется верхним слоем Featured. В Movie без трейлера на Phone первый лейбл смещён с (67; 221) на (16; 16). На Tablet Portrait: (24; 173) → (24; 24).'),
('Бейдж «Спасибо» удалён','Spasibo Badge 66 × 24 при (24; 24) отсутствует в текущих деревьях всех 27 вариантов. Это отдельное изменение, а не переименование labelGroup.'),
('Изменены ограничения логотипа на Phone','Базовый слот без трейлера: 200 × 80 → 130 × 80 (−35% по ширине). С трейлером: 150 × 60 → 95 × 60 (−36,67%). Геометрия вставленной картинки может отличаться от размера слота.'),
('Meta на планшете стала уже','Все 9 базовых Tablet Meta: ширина 526 → 480 (−46; −8,75%). В Featured экземпляры Meta: 502 → 480 (−22), при сохранении ширины Meta+Offer Box 526.'),
('Media изменилась отдельно','Базовая Phone Meta Media: 203 × 192 → 203 × 280. Но её экземпляр в Featured: 360 × 192 → 360 × 194. Разница обусловлена шириной текстового блока и его компоновкой; нельзя переносить +88 на экран.'),
]
spacing=[['Параметр','Было','Стало','Основание'],['Низ PageIndicator / Phone','16','16','391−369−6; 360−338−6'],['PageIndicator / Phone, y','369','338','−31, размер 70 × 6 сохранён'],['Низ PageIndicator / Tablet','24','24','Размер 80 × 8 сохранён'],['Meta+Offer Box: нижнее поле / Phone','40*','40','Геометрия / текущий padding'],['Meta+Offer Box: низ и слева / Tablet','24* / 24*','24 / 24','Геометрия / текущий padding'],['Meta - Text, горизонтальный шаг / Phone','6*','6','Между видимыми текстами'],['Meta - Text, горизонтальный шаг / Tablet','8*','10','+2, Movie / Event / Music / Sport'],['Лейблы Movie, горизонтальный шаг / Phone','4*','4','Размеры лейблов сохранены'],['Лейблы Movie, горизонтальный шаг / Tablet','4*','6','+2'],['Media: заголовок → описание / Phone','6*','8','+2'],['Media: заголовок → описание / Tablet','8*','12','+4'],['Media: тип → автор / Phone','10*','12','+2'],['Media: тип → автор / Tablet','10*','14','+4']]
notes=[
'Источники: «до» — историческое состояние, открытое в Figma Desktop по переданной ссылке с version-id=2389408023268515637; «сейчас» — живой файл VCkyAgp18B3cs0RwzcwHrI. Срез снят 6 октября 2026. Featured: 33779:6834; Meta: 33779:6997.',
'Проверены 27 вариантов Featured и 18 базовых Meta, раскрытые дочерние слои и доступные вложенные запчасти. Текущие скрытые слои выгружены с отключённой фильтрацией. Рендеры сохранены для всех 45 пар.',
'Размеры и координаты — единицы холста Figma, не физические пиксели устройства. Дельта = сейчас − до. В таблицах показаны 2 знака; исходные числа сохранены в JSON. Координаты внутренних слоёв даны относительно родителя. Перемещение варианта на холсте не считается изменением UI.',
'Звёздочка (*) означает измеренное расстояние по геометрии старой версии. Старые свойства Auto Layout, шрифта, привязки к токенам и точные значения цветов не получены: исторический канал отдаёт геометрию и рендеры. Такие значения не выдаются за проверенные свойства. Новые параметры Auto Layout и типографики доступны в подробном HTML.',
'Постеры и часть логотипов заменены. Парные изображения показывают фактический внешний вид обеих версий; это не чистая пиксельная карта изменений компоновки. Зелёные и розовые схемы в HTML сравнивают только границы контейнеров.',
'Некоторые внутренние слои старых инстансов не раскрываются по составному ID. Новые дочерние элементы внутри таких закрытых веток не считаются автоматически добавленными. Сравнение шрифтов, цветов, эффектов, токенов и поведения на произвольной ширине не подтверждено полностью.',
]
FONT=Path('/Users/r.bulatov/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
pdfmetrics.registerFont(TTFont('DV',str(FONT/'DejaVuSans.ttf')));pdfmetrics.registerFont(TTFont('DVB',str(FONT/'DejaVuSans-Bold.ttf')))
PDF=P.parent/'pdf'/'featured-meta-visual-diff.pdf';cv=canvas.Canvas(str(PDF),pagesize=(595.28,841.89));W,H=595.28,841.89;page=0
style=ParagraphStyle('body',fontName='DV',fontSize=9,leading=13,textColor=HexColor('#273246'))
def txt(text,x,y,width,size=9,bold=False,color='#273246'):
 st=ParagraphStyle('x',parent=style,fontName='DVB'if bold else'DV',fontSize=size,leading=size*1.4,textColor=HexColor(color))
 p=Paragraph(html.escape(text).replace('\n','<br/>'),st);_,h=p.wrap(width,800);p.drawOn(cv,x,y-h);return y-h

def start(heading,sub=''):
 global page
 if page:cv.showPage()
 page+=1;cv.setFillColor(HexColor('#FAFBFF'));cv.rect(0,0,W,H,fill=1,stroke=0)
 cv.setFillColor(HexColor('#7138F5'));cv.rect(28,H-32,34,4,fill=1,stroke=0)
 txt('OKKO / FEATURED + META',72,H-23,430,8,True,'#7138F5')
 y=txt(heading,28,H-54,539,21,True)
 if sub:y=txt(sub,28,y-8,539,8)
 txt('06.10.2026  •  Сравнение двух состояний Figma',28,24,450,7,color='#738095');txt(str(page),540,24,25,7)
 return y-22

def table(rows,y,widths,size=8):
 x=28
 for ri,row in enumerate(rows):
  hs=[]
  for ci,(v,w) in enumerate(zip(row,widths)):
   p=Paragraph(html.escape(str(v)),ParagraphStyle('t',parent=style,fontName='DVB'if ri==0 else'DV',fontSize=size,leading=size*1.3));_,h=p.wrap(w-10,700);hs.append((p,h))
  hh=max(h for _,h in hs)+12
  cv.setFillColor(HexColor('#EBE6FA'if ri==0 else('#FFFFFF'if ri%2 else'#F0F3F8')));cv.rect(x,y-hh,sum(widths),hh,fill=1,stroke=0)
  xx=x
  for ci,((p,h),w) in enumerate(zip(hs,widths)):
   if ri and len(row)==4 and differs(row[1],row[2]) and ci in [1,2,3]:
    cv.setFillColor(HexColor('#FFE5EB' if ci==1 else '#DDF8EE' if ci==2 else '#FFF0CC'));cv.rect(xx,y-hh,w,hh,fill=1,stroke=0)
   p.drawOn(cv,xx+5,y-6-h);xx+=w
  y-=hh
 return y

y=start('Что изменилось','27 вариантов Featured • 18 вариантов Meta • полный реестр измерений в HTML')
y=txt('Цветные контуры: оранжевый — размер/положение; розовый пунктир — удалено; зелёный — добавлено. Таблицы: розовый — до, зелёный — сейчас, жёлтый — разница. Скрытые слои отмечены только в таблицах.',28,y,539,9)-16
for heading,body in summary:
 y=txt(heading,28,y,539,11,True)-5;y=txt(body,28,y,539,10)-18

y=start('Отступы и расположение','* Старое значение вычислено по геометрии; новое проверено в текущей структуре.')
y=table(spacing,y,[240,65,65,169],8)-18
y=txt('Новый верхний labelGroup',28,y,539,12,True)-7
y=txt('Phone: padding сверху/слева 16, справа 72, снизу 0. Высота 36 для обычных лейблов и 56 для спорта. Tablet: сверху/слева 24, справа 72, снизу 0; высота 48 и 70 соответственно. Спортивная группа имеет itemSpacing 0.',28,y,539,10)-16
y=txt('Сохранено',28,y,539,12,True)-7
y=txt('Кнопки звука: Phone 36 × 36, Tablet 40 × 40, отступ сверху/справа 24. Пагинация сохраняет размеры и отступ от нижней границы. Meta+Offer Box сохраняет нижнее поле 40 на Phone и 24 на Tablet. Его высота и y меняются вслед за содержимым.',28,y,539,10)

y=start('Матрица размеров Meta','Это базовые запчасти; размеры экземпляров в Featured приведены на последующих страницах.')
rows=[['Вариант','Было W × H','Стало W × H','ΔW / ΔH']]
for id in meta:
 a,b=O[id],C[id];rows.append([title(b),dims(a),dims(b),fmt(b['width']-a['width'])+' / '+fmt(b['height']-a['height'])])
y=table(rows,y,[259,95,95,90],7.5)

y=start('Вложенные слои и точность')
for heading,body in [
 ('Логотип: слот и содержимое','В Movie Phone без трейлера сам слот в экземпляре меняется 200 × 66,48 → 130 × 52; соотношение 3,008 → 2,5. Базовый слот той же Meta имеет другое соотношение: 2,5 → 1,625. Изменение слота не доказывает растяжение изображения.'),
 ('Скрытые состояния','В базовых Movie и Event для Phone/Tablet появились скрытые Promo Text. В Phone скрытый Text Name: высота 56 → 84. В Sport Teams добавлен скрытый Text Name. Скрытые кнопки оффера и скрытые строки спорта учтены в HTML, но не влияют на показанные рендеры.'),
 ('Meta Media','Phone: заголовок 203 × 84 → 203 × 126, описание 203 × 66 → 203 × 110. Tablet: заголовок 420 × 92 без изменения; описание 454 × 52 → 454 × 78. Аватары остаются 22 × 22 / 24 × 24. Ряд автора: 203 → 205 / 228 → 232 по ширине.'),
 ('Текст метаданных','Высота текстовых слоёв года/жанра/времени/ценза: Phone 18 → 20, Tablet 20 → 22. Сейчас это Suisse Int’l Medium 15/20 и 17/22. Старый fontSize не подтверждён; высота слоя не выдаётся за размер шрифта.'),
 ('Обнаруженные особенности','В базовой Phone Event строка Meta - Text шириной 238 содержит видимые элементы от x=−17 до x=255: выход по 17 с каждой стороны. В Meta Media Phone ряд автора шириной 205 расположен при x=−1 внутри ширины 203. Это фактическая геометрия, а не утверждение об ошибке в продакшне.'),
]:y=txt(heading,28,y,539,11,True)-4;y=txt(body,28,y,539,9)-15

def pair(id,y,maxh=175):
 a,b=O[id],C[id];name=title(b);y=txt(name,28,y,539,11,True)-5
 y=txt('Узел '+id+'  |  '+dims(a)+' → '+dims(b),28,y,539,8)-9
 scale=min(251/max(a['width'],b['width']),maxh/max(a['height'],b['height']))
 for j,pre in enumerate(['old','new']):
  n=a if j==0 else b;x=28+j*279;txt('ДО'if j==0 else'СЕЙЧАС',x,y,251,8,True,'#A73561'if j==0 else'#168477')
  im=Image.open(P/'assets'/f'{pre}-{id.split(":")[1]}.png');iw=n['width']*scale;ih=n['height']*scale
  cv.setFillColor(HexColor('#20232B'));cv.rect(x,y-18-maxh,251,maxh,fill=1,stroke=0)
  cv.drawImage(ImageReader(im),x+(251-iw)/2,y-18-ih,iw,ih,mask='auto')
  pdf_marks(id,pre,x+(251-iw)/2,y-18,scale)
 y-=maxh+28
 rows=[['Измерение','До','Сейчас','Δ']]
 if id in featured:
  for name in ['Meta+Offer Box','Meta']:
   aa=find(a,name);bb=find(b,name)
   if aa and bb:rows.append([name+' / W × H',dims(aa),dims(bb),fmt(bb['width']-aa['width'])+' / '+fmt(bb['height']-aa['height'])])
  aa=find(a,'Meta+Offer Box');bb=find(b,'Meta+Offer Box');rows.append(['Meta+Offer Box / y',fmt(aa['y']),fmt(bb['y']),fmt(bb['y']-aa['y'])])
 else:
  for name in ['Logo Title Img','Text Box','Meta - Text','Meta - Text Group','Meta media','Text Name']:
   aa=find(a,name);bb=find(b,name)
   if aa and bb and aa.get('visible') and bb.get('visible'):rows.append([name+' / W × H',dims(aa),dims(bb),fmt(bb['width']-aa['width'])+' / '+fmt(bb['height']-aa['height'])])
 return table(rows[:4],y,[229,110,110,90],7)-20
for group,label,maxh in [(featured,'Featured: визуальное сравнение',160),(meta,'Meta: визуальное сравнение',145)]:
 for i in range(0,len(group),2):
  y=start(label,'Контуры: оранжевый — геометрия; розовый пунктир — удалено; зелёный — добавлено.')
  y=pair(group[i],y,maxh)
  if i+1<len(group):y=pair(group[i+1],y,maxh)

y=start('Источники и границы проверки')
for s in notes:y=txt(s,28,y,539,10)-19
url='https://www.figma.com/design/VCkyAgp18B3cs0RwzcwHrI/Lib-Android-Mobile?node-id=33779-6834'
y=txt('Открыть версию «до» в Figma',28,y,539,10,True)-12;cv.linkURL(url+'&version-id=2389408023268515637',(28,y,560,y+28),relative=0)
y=txt('Открыть текущее состояние в Figma',28,y,539,10,True);cv.linkURL(url,(28,y,560,y+15),relative=0)
cv.save()
# Fully self-contained detailed document.
def image_uri(id,prefix):return 'data:image/png;base64,'+base64.b64encode((P/'assets'/f'{prefix}-{id.split(":")[1]}.png').read_bytes()).decode()
def htable(rows):
 out='<table>'
 for i,r in enumerate(rows):
  out+='<tr>'
  for j,c in enumerate(r):
   bg=''
   if i and len(r)==4 and differs(r[1],r[2]) and rows[0][1] not in ['Изменение']:
    bg={1:'#FFE5EB',2:'#DDF8EE',3:'#FFF0CC'}.get(j,'')
   if i and len(r)==7 and rows[0][2]=='Свойство':bg={3:'#FFE5EB',4:'#DDF8EE',5:'#FFF0CC'}.get(j,'')
   if i and len(r)==4 and rows[0][1]=='Изменение':bg='#FFE5EB' if 'Вышел' in str(r[1]) else '#DDF8EE'
   tag='th' if i==0 else 'td';out+=f'<{tag} style="background:{bg}">'+html.escape(str(c))+f'</{tag}>'
  out+='</tr>'
 return out+'</table>'

def schematic(id):
 a,b=O[id],C[id];ww=max(a['width'],b['width']);hh=max(a['height'],b['height']);s=f'<svg viewBox="0 0 {ww} {hh}" aria-label="Геометрическое наложение" style="max-height:300px;width:100%">'
 for root,color in [(a,'#d8467b'),(b,'#0daf98')]:
  for n,path,v,x,y in flatten(root):
   if not v or (n is not root and n['name']not in ['Meta+Offer Box','Meta','labelGroup','Logo Title Img','Text Box','Meta - Text','Meta - Text Group','Meta media']):continue
   s+=f'<rect x="{x}" y="{y}" width="{n["width"]}" height="{n["height"]}" fill="none" stroke="{color}" stroke-width="1.5"><title>{html.escape(n["name"])}: {dims(n)}; x={fmt(x)}, y={fmt(y)}</title></rect>'
 return s+'</svg>'
parts=['''<!doctype html><html lang="ru"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Featured + Meta — визуальный диф</title><style>body{margin:0;background:#f3f5fa;color:#202b40;font:15px/1.6 -apple-system,BlinkMacSystemFont,Arial,sans-serif}main{max-width:1200px;margin:auto;padding:36px}header,section{background:white;border-radius:16px;padding:28px;margin-bottom:24px}h1{font-size:40px;line-height:1.15}h2{margin-top:0}h3{font-size:20px}small,.muted{color:#637083}table{width:100%;border-collapse:collapse;font-size:12px;margin:16px 0;table-layout:auto}td,th{text-align:left;vertical-align:top;padding:9px;border-bottom:1px solid #e4e9f1;overflow-wrap:anywhere}th{background:#eee7fd}td:first-child{max-width:350px}button,input{font:inherit;padding:10px 14px;border:1px solid #ccd3e3;border-radius:9px;background:white}nav{position:sticky;top:0;background:#f3f5faf5;padding:12px 0;z-index:1}.pair{display:grid;grid-template-columns:1fr 1fr;gap:16px}.visual{background:#20232b;padding:18px;display:flex;align-items:flex-start;justify-content:center;min-height:160px}.visual img{max-width:100%;object-fit:contain;object-position:top}details{margin:16px 0}summary{cursor:pointer;font-weight:600}.tag{color:#7138f5;font-weight:700}a{color:#7138f5}.old{color:#c02f68}.new{color:#078473}.overflow{overflow-x:auto}@media print{nav{display:none}section{break-before:page}details{display:block}body{background:white}}@media(max-width:700px){main{padding:12px}.pair{grid-template-columns:1fr}h1{font-size:28px}}</style><main><header><span class="tag">OKKO • ANDROID MOBILE • 06.10.2026</span><h1>Featured + Meta<br>Что изменилось</h1><p><b>Цветные отметки:</b> 🟠 изменились размер или положение · 🩷 пунктир: удалено из ветки · 🟢 добавлено в ветку. Скрытые слои выделены только в таблицах. В таблицах: розовый — было, зелёный — стало, жёлтый — разница.</p><p>27 вариантов Featured и 18 запчастей Meta. Визуальное сравнение, точная геометрия вложенных слоёв и текущие параметры компоновки.</p>''']
for h,t in summary:parts.append('<h3>'+h+'</h3><p>'+t+'</p>')
parts.append('</header><section><h2>Методика и границы точности</h2>'+''.join('<p>'+html.escape(n)+'</p>'for n in notes)+f'<p><a href="{url}&version-id=2389408023268515637">Источник «до»</a> · <a href="{url}">Сейчас</a></p></section>')
parts.append('<section><h2>Отступы</h2>'+htable(spacing)+'</section><nav><input id="filter" placeholder="Найти: Phone, Media, 33779:6998…" style="width:60%"> <button onclick="document.querySelectorAll(\'details\').forEach(x=>x.open=true)">Раскрыть таблицы</button> <button onclick="document.querySelectorAll(\'.marks\').forEach(x=>x.style.visibility=x.style.visibility===\'hidden\'?\'visible\':\'hidden\')">Показать / скрыть отметки</button></nav>')
for id in ids:
 a,b=O[id],C[id];kind='Featured'if id in featured else'Meta';name=title(b)
 parts.append(f'<section class="variant" data-search="{html.escape(kind+" "+name+" "+id)}"><span class="tag">{kind} · {id}</span><h2>{html.escape(name)}</h2><p>{dims(a)} → {dims(b)} · ΔW {fmt(b["width"]-a["width"])} · ΔH {fmt(b["height"]-a["height"])} · W/H {a["width"]/a["height"]:.4f} → {b["width"]/b["height"]:.4f}</p><div class="pair">')
 scale=min(500/max(a['width'],b['width']),330/max(a['height'],b['height']))
 for prefix,n,label in [('old',a,'ДО'),('new',b,'СЕЙЧАС')]:parts.append(f'<div><b>{label}</b><div class="visual"><div style="position:relative;line-height:0"><img alt="{html.escape(name)} — {label}" src="{image_uri(id,prefix)}" style="width:{n["width"]*scale}px;height:{n["height"]*scale}px">{overlay_svg(id,prefix)}</div></div></div>')
 parts.append('</div><details><summary>Геометрическое наложение без постеров</summary><p><span class="old">Розовый — до</span> · <span class="new">зелёный — сейчас</span>. Наведите курсор на контур для размеров.</p>'+schematic(id)+'</details>')
 rows=[['Слой / путь','ID','Свойство','До','Сейчас','Δ','Состояние']]+allchanges[id]
 parts.append(f'<details open><summary>Изменения геометрии: {len(rows)-1}</summary><p class="muted">x/y относительно родителя; учитываются скрытые слои. Данные основываются на совпадающих ID.</p><div class="overflow">'+htable(rows)+'</div></details>')
 # Structural observations only for parents whose child trees were actually expanded before.
 om={n['id']:n for n,_,_,_,_ in flatten(a)};cm={n['id']:n for n,_,_,_,_ in flatten(b)};struct=[]
 for n,path,v,_,_ in flatten(b):
  old=om.get(n['id'])
  if not old or not old.get('children'):continue
  oldch={x['id']:x for x in old['children']};newch={x['id']:x for x in n.get('children',[])}
  for k,x in oldch.items():
   if k not in newch:struct.append([path,'Вышел из дочерних слоёв',x['name'],k])
  for k,x in newch.items():
   if k not in oldch:struct.append([path,'Появился среди дочерних слоёв',x['name'],k])
 parts.append('<details><summary>Изменения состава раскрытых веток</summary>'+htable([['Родитель','Изменение','Слой','ID']]+struct)+'</details>')
 rows=[['Слой','ID','Режим / размер','Padding T/R/B/L','Gap','Шрифт / интерлиньяж','Видимость']]
 for n,path,v,_,_ in flatten(b):
  if n.get('type')not in ['FRAME','COMPONENT','INSTANCE','TEXT','SLOT']:continue
  fn=n.get('fontName',{});font=(fn.get('family','')+' '+fn.get('style','')+' '+fmt(n.get('fontSize'))+' / '+fmt(n.get('lineHeight',{}).get('value'))).strip()if n['type']=='TEXT'else''
  rows.append([path.split(' / ',1)[-1],n['id'],str(n.get('layoutMode',''))+' '+n.get('layoutSizingHorizontal','')+'/'+n.get('layoutSizingVertical',''),'/'.join(fmt(n.get(k))for k in ['paddingTop','paddingRight','paddingBottom','paddingLeft']),fmt(n.get('itemSpacing')),font,'видим'if v else'скрыт'])
 parts.append('<details><summary>Все текущие параметры вложенных слоёв</summary>'+htable(rows)+'</details></section>')
parts.append('''<script>document.getElementById('filter').addEventListener('input',e=>{let q=e.target.value.toLowerCase();document.querySelectorAll('.variant').forEach(s=>s.hidden=!s.dataset.search.toLowerCase().includes(q))});</script></main></html>''')
(P/'featured-meta-diff.html').write_text(''.join(parts))
print(json.dumps({'pdf':str(PDF),'pages':page,'html':str(P/'featured-meta-diff.html'),'geometry_changes':sum(map(len,allchanges.values()))},ensure_ascii=False))
