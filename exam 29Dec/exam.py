import urllib.request
import os
import re

def download_page(page_url):
    try:
        user_a = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        req = urllib.request.Request(page_url, headers={'User-Agent':user_a})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except:
        return
    return html


def find_data(html):
    regexp = re.compile('<html.*?</html>', flags = re.U | re.DOTALL)
    lst = regexp.findall(html)
    reg_clean_0 = re.compile('<!--.*?-->', flags = re.U | re.DOTALL)
    reg_clean_1 = re.compile('<script.*?</script>', flags = re.U | re.DOTALL)
    reg_clean_2 = re.compile('<.*?>', flags = re.U | re.DOTALL)
    reg_clean_3 = re.compile('&.*?;', flags = re.U | re.DOTALL)
    
    t = reg_clean_0.sub(" ", lst[0])
    t = reg_clean_1.sub(" ", t)
    t = reg_clean_2.sub(" ", t)
    t = reg_clean_3.sub(" ", t)

    return t



fin = open('input.txt', 'w', encoding='utf-8')

url = 'http://web-corpora.net/Test2_2016/short_story.html'
html = download_page(url)

dct = {}
s = find_data(html)
a = s.split(' ')
for i in a:
    if len(i) != 0:
        if i != '\n':
            dct[i.lower()]=0
print(dct, file = fin)
text = ''
for key in dct:
    if key[0]=='с':
        word = ''
        for k in key:
            if ord('а')<= ord(k) <= ord('я'):
                word += k
        text += word + '\n'       
fin.close()


fout = open('input.txt', 'w', encoding='utf-8')
print(text, file = fout)
fout.close()
#в файле 'input.txt' - все слова на букву "с", распечатанные в столбик

fout = open('input.txt', 'r', encoding='utf-8')
for line in fout:
    print(line, end='')
fout.close()

os.system(r"C:\Users\Tanya\Downloads\mystem.exe C:\Users\Tanya\Desktop\input.txt C:\Users\Tanya\Desktop\output.txt -ni")

fin = open('output.txt', 'r', encoding='utf-8')

for line in fin:
    lst = line.split('{')
    word = lst[0]

    l = lst[1].split('=')
    lemma = l[0]
    speech_part = l[1].split(',')[0]

    if speech_part == 'V':
        print(word) #выводим на экран глаголы
fin.close()


fin = open('output.txt', 'r', encoding='utf-8')
fout = open('sql.txt', 'w', encoding='utf-8')
print('CREATE TABLE my_table (id INTEGER PRIMARY KEY, lemma VARCHAR(100), word VARCHAR(100), speech_part VARCHAR(100));', file=fout)
row = 'INSERT INTO my_table (id, lemma, word, speech_part) VALUES (%d, \'%s\', \'%s\', \'%s\');'

num = 0
for line in fin:
    lst = line.split('{')
    word = lst[0]

    l = lst[1].split('=')
    lemma = l[0]
    speech_part = l[1].split(',')[0]
        
    print(row % (num, lemma, word, speech_part), file = fout)
    num += 1

fout.close()
fin.close()

#в файле sql.txt - код для создания и заполнения таблицы sql
#output.txt - разметка mystem'ом всех слов на "с"



