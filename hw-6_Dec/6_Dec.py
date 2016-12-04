import json
import urllib.request
import html
import re
import time
import os

links=[]

def download_page(page_url):
    try:
        #time.sleep(2)
        user_a = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        req = urllib.request.Request(page_url, headers={'User-Agent':user_a})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except:
        return
    return html

def find_metadata(html, r, r1, r2, r3):
    regexp = re.compile(r, flags = re.U | re.DOTALL)
    lst = regexp.findall(html)
    t = lst[0]
    reg_clean_1 = re.compile(r1, flags=re.U | re.DOTALL)
    reg_clean_2 = re.compile(r2, flags=re.U | re.DOTALL)
    reg_clean_3 = re.compile(r3, flags=re.U | re.DOTALL)
    reg_clean_4 = re.compile('[\?!,\.\n]', flags=re.U | re.DOTALL)
    reg_clean_5 = re.compile(' \- ', flags=re.U | re.DOTALL)
    
    clean_t = reg_clean_1.sub("", t)
    clean_t = reg_clean_2.sub("", clean_t)
    clean_t = reg_clean_3.sub("", clean_t)
    clean_t = reg_clean_4.sub(" ", clean_t)
    clean_t = reg_clean_5.sub(" ", clean_t)

    return clean_t

def unique(paper, name):
    a=[]
    for i in paper:
        n = common_lst[name].index(i)
        if (n != len(common_lst[name]) - 1) and (common_lst[name][n] == common_lst[name][n+1]) and (common_lst[name][n] != ''):
            a.append(i)
    return a

links={'regnum':'https://regnum.ru/news/society/2213203.html', 'izv':'http://izvestia.ru/news/649332', 'kp':'http://www.kp.ru/online/news/2589020/', 'tass':'http://tass.ru/nauka/3838714'}
news={}

for key in links:
    r = r1 = r2 = r3 = ''
    html = download_page(links[key])
    if key == 'regnum':
        r = '<a class="news_detail_template_date" href=.*?<em>'
        r1 = '<a class="news_detail_template_date" href=.*?</b></span>'
        r2 = '<.*?>'
        r3 = '&.*?;'
    if key == 'izv':
        r = '<p class="copy">Фото: TASS/PA Images/Chris Radburn</p>.*?<p>Читайте также:'
        r1 = '<p class="copy">Фото: TASS/PA Images/Chris Radburn</p>'
        r2 = '<.*?>'
        r3 = 'Читайте также:'
    if key == 'kp':
        r = '<div class="text" itemprop="articleBody" id="hypercontext">.*?</article><div class="externalBlock">'
        r1 = '<.*?>'
    if key == 'tass':
        r = '<div class="b-material-text__l js-mediator-article">.*?<div class="extra-content">'
        r1 = '<.*?>'
        r2 = 'РИМ, 3 декабря. /Корр. ТАСС Вера Щербакова/.'
        r3 = '\xa0'
    news[key] = find_metadata(html, r, r1, r2, r3)


common_set={}
common_lst={}
for key in news:
    common_lst[key] = news[key].split(' ')
    common_lst[key].sort()
    
    common_set[key] = set(common_lst[key])
    common_set[key].discard('')

cross = common_set['kp']
for key in common_set:
    cross = common_set[key]&cross
cr = list(cross)
cr.sort()
f_cross = open('f_cross.txt', 'w')
for i in cr:
    print(i, file = f_cross)
f_cross.close()

s = common_set['kp'] | common_set['regnum'] | common_set['tass'] | common_set['izv']
s_izv = common_set['kp'] | common_set['regnum'] | common_set['tass']
s_tass = common_set['kp'] | common_set['regnum'] | common_set['izv']
s_regnum = common_set['kp'] | common_set['tass'] | common_set['izv']
s_kp = common_set['regnum'] | common_set['tass'] | common_set['izv']

izv = list(s - s_izv)
tass = list(s - s_tass)
regnum = list(s - s_regnum)
kp = list(s - s_kp)

izv.sort()
tass.sort()
regnum.sort()
kp.sort()

f = open('izv.txt', 'w')
for i in izv:
    print(i, file = f)
f.close()

f = open('tass.txt', 'w')
for i in tass:
    print(i, file = f)
f.close()

f = open('regnum.txt', 'w')
for i in regnum:
    print(i, file = f)
f.close()

f = open('kp.txt', 'w')
for i in kp:
    print(i, file = f)
f.close()


f = open('unique_izv.txt', 'w')
k = unique(izv, 'izv')
if len(k) == 0:
    print('Все словоформы в данной статье уникальны - словоформ с частотностью больше 1 нет', file = f)
else:
    for i in k:
        print(i, file = f)
f.close()

f = open('unique_tass.txt', 'w')
k = unique(tass, 'tass')
if len(k) == 0:
    print('Все словоформы в данной статье уникальны - словоформ с частотностью больше 1 нет', file = f)
else:
    for i in k:
        print(i, file = f)
f.close()

f = open('unique_regnum.txt', 'w')
k = unique(regnum, 'regnum')
if len(k) == 0:
    print('Все словоформы в данной статье уникальны - словоформ с частотностью больше 1 нет', file = f)
else:
    for i in k:
        print(i, file = f)
f.close()

f = open('unique_kp.txt', 'w')
k = unique(kp, 'kp')
if len(k) == 0:
    print('Все словоформы в данной статье уникальны - словоформ с частотностью больше 1 нет', file = f)
else:
    for i in k:
        print(i, file = f)
f.close()

