import urllib.request
import html
import re
import time
import os


def download_page(page_url):
    try:
        time.sleep(2)
        user_a = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        req = urllib.request.Request(page_url, headers={'User-Agent':user_a})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except:
        return
    return html

def find_metadata_au(url, html):
    regexp = re.compile('<meta property="article:author".*?/>', flags = re.U | re.DOTALL)
    titles = regexp.findall(html)
    if len(titles) == 0:
        row = 'Noname'
    else:
        t = titles[0]
        reg_clean_1 = re.compile('<meta property="article:author" content="', flags=re.U | re.DOTALL)
        reg_clean_2 = re.compile('"/>', flags=re.U | re.DOTALL)
        clean_t = reg_clean_1.sub("", t)
        clean_t = reg_clean_2.sub("", clean_t)
        row = clean_t
    return row
        
        

def find_metadata_ti(url, html):
    regexp = re.compile('<meta property="og:title".*?/>', flags = re.U | re.DOTALL)
    titles = regexp.findall(html)
    if len(titles) == 0:
        row = 'Noname'
    else:
        t = titles[0]
        reg_clean_1 = re.compile('<meta property="og:title" content="', flags = re.U | re.DOTALL)
        reg_clean_2 = re.compile('"/>', flags = re.U | re.DOTALL)
        clean_t = reg_clean_1.sub("", t)
        clean_t = reg_clean_2.sub("", clean_t)
        row = clean_t
    return row

    
def find_metadata_da(url, html):
    regexp = re.compile('<a href="/ural/\d{4}/\d{1,2}">', flags = re.U | re.DOTALL)
    titles = regexp.findall(html)
    if len(titles) == 0:
        row = 'Noname'
    else:
        t = titles[0]
        reg_clean_1 = re.compile('<a href="/ural/', flags = re.U | re.DOTALL)
        reg_clean_2 = re.compile('">', flags = re.U | re.DOTALL)
        clean_t = reg_clean_1.sub("", t)
        clean_t = reg_clean_2.sub("", clean_t)
        row = clean_t[len(clean_t)-2:len(clean_t)] + '.' + clean_t[0:4]
        if row[0] == '/':
            row = row[1:]
    return row


def find_metadata_url(url, html):
    regexp = re.compile('<meta property="og:url".*?/>', flags = re.U | re.DOTALL)
    titles = regexp.findall(html)
    if len(titles) == 0:
        row = 'Noname'
    else:
        t = titles[0]
        reg_clean_1 = re.compile('<meta property="og:url" content="', flags = re.U | re.DOTALL)
        reg_clean_2 = re.compile('"/>', flags=re.U | re.DOTALL)
        clean_t = reg_clean_1.sub("", t)
        clean_t = reg_clean_2.sub("", clean_t)
        row = clean_t
    return row
        

def find_metadata_text(url, html):
    regexp = re.compile('<div class="body_contents">.*?</div>', flags = re.U | re.DOTALL)
    titles = regexp.findall(html)
    if len(titles) == 0:
        return
    else:
        t = titles[0]
        reg_clean_1 = re.compile('&.*?;', flags = re.U | re.DOTALL)
        reg_clean_2 = re.compile('<.*?>', flags = re.U | re.DOTALL)
        clean_t = reg_clean_1.sub("", t)
        clean_t = reg_clean_2.sub("", clean_t)
        return clean_t


common_url_1 = 'http://magazines.russ.ru/ural/'
common_url_2 = 'http://magazines.russ.ru'

new_titles = []
for i in range(1996, 1999):
    for j in range(1, 13):
        url = common_url_1 + str(i) + '/' + str(j)
        html = download_page(url)
        if html != None:
            rex = re.compile('<a href="/ural/\d{4}/\d{1,2}/[a-zA-Z0-9]+.html"', flags = re.U | re.DOTALL)
            titles = rex.findall(html)
            reg_clean_1 = re.compile('<a href="', flags = re.U | re.DOTALL)
            reg_clean_2 = re.compile('"', flags = re.U | re.DOTALL)
            for t in titles:
                clean_t = reg_clean_1.sub("", t)
                clean_t = reg_clean_2.sub("", clean_t)
                new_titles.append(common_url_2 + clean_t)
    url = common_url_1 + str(i) + '/' + '11-12'
    html = download_page(url)
    if html != None:
        rex = re.compile('<a href="/ural/\d{4}/11-12/[a-zA-Z0-9]+.html">.+</a>', flags = re.U | re.DOTALL)
        titles = rex.findall(html)
        reg_clean_1 = re.compile('<a href="', flags = re.U | re.DOTALL)
        reg_clean_2 = re.compile('">.*?</a>', flags = re.U | re.DOTALL)
        for t in titles:
            clean_t = reg_clean_1.sub("", t)
            clean_t = reg_clean_2.sub("", clean_t)
            new_titles.append(common_url_2 + clean_t)

        
common_direction = os.sep + "Users" + os.sep + "Tanya" + os.sep + "gazeta"

if not os.path.exists(common_direction):
        os.makedirs(common_direction)
fout_csv = open(common_direction + os.sep + "metadata.csv", 'w')

row_csv = ''
for i in range(23):
    row_csv += '%s\t'
print(row_csv % ('path', 'author', 'sex', 'birthday', 'header', 'created', 'sphere', 'genre_fi', 'type', 'topic', 'chronotop', 'style', 'audience_age', 'audience_level', 'audience_size', 'source', 'publication', 'publisher', 'publ_year', 'medium', 'country', 'region', 'language'), file = fout_csv)

ct = 0
for i in new_titles:
    pg = download_page(i)
        
    au = find_metadata_au(i, pg)
    ti = find_metadata_ti(i, pg)
    da = find_metadata_da(i, pg)
    url = find_metadata_url(i, pg)
    text = find_metadata_text(i, pg)
        
    month = da[0:len(da)-5]
    year = da[len(da)-4:len(da)]

    dir_1 = common_direction + os.sep + "plain" + os.sep + year + os.sep + month
    dir_2 = common_direction + os.sep + "mystem-xml" + os.sep + year + os.sep + month
    dir_3 = common_direction + os.sep + "mystem-plain" + os.sep + year + os.sep + month

    if not os.path.exists(dir_1):
        os.makedirs(dir_1)
    if not os.path.exists(dir_2):
        os.makedirs(dir_2)
    if not os.path.exists(dir_3):
        os.makedirs(dir_3)

    lst = os.listdir(dir_1)
    num = len(lst) + 1
    fout = open(dir_1 + os.sep + "article" + str(num) + ".txt", 'w', encoding='utf-8')
    print(text, file = fout)
    fout.close()

    lst = os.listdir(dir_1)
    for i in lst:
        os.system(r"C:\Users\Tanya\Downloads\mystem.exe " +  dir_1 + os.sep + i + " " + dir_3 + os.sep + i + " encoding='utf-8'" + " -di")
        fl = i[0:len(i)-3]
        fl += 'xml'
        os.system(r"C:\Users\Tanya\Downloads\mystem.exe " +  dir_1 + os.sep + i + " " + dir_2 + os.sep + fl + " encoding='utf-8'" + " -di --format xml")
        
    fout = open(dir_1 + os.sep + "article" + str(num) + ".txt", 'w', encoding='utf-8')
    print('@au', au, file = fout)
    print('@ti', ti, file = fout)
    print('@da', da, file = fout)
    print('@url', url, file = fout)
    print(text, file = fout)
    fout.close()

    path = dir_1 + os.sep + "article" + str(num) + ".txt"
    print(row_csv % (path, au, '', '', ti, da, 'публицистика', '', '', '', '', 'нейтральный', 'н-возраст', 'н-уровень', 'городская', url, 'Урал', '', year, 'газета', 'Россия', 'г.Екатеринбург, Свердловская обл-ть', 'ru'), file = fout_csv)
    
fout_csv.close()


