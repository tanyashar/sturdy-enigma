import json
import urllib.request
import html
import re
import time
import os

dct={}
dct2={}

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

def find_metadata(url, html):
    regexp = re.compile('<tr><td class=th><a href=\'.*?\'>.*?</a>.*?<td>.*?</td></tr>', flags = re.U | re.DOTALL)
    lst = regexp.findall(html)
    for t in lst:  
        reg_clean_1 = re.compile('<tr><td class=th><a href=\'.*?\'>', flags=re.U | re.DOTALL)
        reg_clean_2 = re.compile('</a>.*?<td>.*?</td></tr>', flags=re.U | re.DOTALL)
        clean_t = reg_clean_1.sub("", t)
        clean_t = reg_clean_2.sub("", clean_t)
        thai = clean_t

        reg_clean_1 = re.compile('<tr><td class=th><a href=\'.*?\'>.*?</a>.*?<td class=pos>.*?<td>', flags=re.U | re.DOTALL)
        reg_clean_2 = re.compile('<.*?>', flags=re.U | re.DOTALL)
        reg_clean_3 = re.compile('&#[0-9a-zA-Z]*;', flags=re.U | re.DOTALL)
        clean_t = reg_clean_1.sub("", t)
        clean_t = reg_clean_2.sub("", clean_t)
        clean_t = reg_clean_3.sub("", clean_t)
        eng = clean_t

        dct[thai] = eng.split(';')

        a=[]
        if dct2.get(thai) != None:
            a = dct2[eng]
        a.append(thai)
        dct2[eng] = a
    return 

common_url = 'file:///D:/Downloads/thai_pages/'

for i in range(187, 206):
    for j in range(0, 99):
        page_url = common_url + str(i) + '.' + str(j) + '.html'
        #print(page_url)
        html = download_page(page_url)
        if html!= None:
            find_metadata(page_url, html)

json.dump(dct, open('thai-eng.json', 'w'))
json.dump(dct2, open('eng-thai.json', 'w'))




