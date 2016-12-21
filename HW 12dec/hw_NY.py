import os
import re

def clean(t, s):
    reg_clean = re.compile(s, flags=re.U | re.DOTALL)
    reg_clean_1 = re.compile('\n', flags=re.U | re.DOTALL)
    
    clean_t = reg_clean_1.sub("", t)
    clean_t = reg_clean.sub("", clean_t)
    
    return clean_t

common_dir = "C:" + os.sep + "Users" + os.sep + "Tanya" + os.sep + "Desktop" + os.sep

os.system(r"C:" + os.sep + "Users" + os.sep + "Tanya" + os.sep + "Downloads" + os.sep + "mystem.exe " + common_dir + "input.txt " + common_dir + "output_mystem.txt " + "encoding='utf-8' " + "-nc")

fin = open('output_mystem.txt', 'r', encoding='UTF-8')
fout_1 = open('output_sql_1.txt', 'w', encoding='UTF-8')
fout_2 = open('output_sql_2.txt', 'w', encoding='UTF-8')

print('CREATE TABLE six_col (id_1 INTEGER PRIMARY KEY, form_1 VARCHAR(100), left VARCHAR(100), right VARCHAR(100), num INTEGER, id_2 INTEGER);', file = fout_1)
print('CREATE TABLE three_col (id_2 INTEGER PRIMARY KEY, form_2 VARCHAR(100), lemma VARCHAR(100));', file = fout_2)

lst=[]
for line in fin:
    lst.append(clean(line, ''))

num = 0
id_1 = 0
id_2 = 0
dct = {}
i = 0
while i != len(lst) - 2:
    if i == len(lst) - 1:
        break
    num += 1
    c = lst[i + 2]
    if i == 0:
        if ord('а') <= ord(lst[0][0]) <= ord('я') or ord('А') <= ord(lst[0][0]) <= ord('Я'):
            a = ''
            b = lst[0]
            c = lst[1]
            i += 1
        else:
            a = lst[0]
            b = lst[1]
            c = lst[2]
            i += 2
    else:
        a = lst[i]
        b = lst[i + 1]
        i += 2

    b1 = b.split('{')
    
    k = clean(b1[1], '}')
    b1.pop()
    b1.append(k)
    
    form_1 = b1[0]
    left = clean(a, '_')
    right = clean(c, '_')
    id_1 = num - 1
    
    k = b1[1]
    y = k.split('|')
    lemma = y[0]
    form_2 = b1[0].lower()

    s = form_2 + ' ' + lemma
    if dct.get(s) == None:
        dct[s] = len(dct)
        id_2 = dct[s]
        row = 'INSERT INTO three_col (id_2, form_2, lemma) VALUES (%d, \'%s\', \'%s\');'
        print(row % (id_2, form_2, lemma), file = fout_2)
    
    id_2 = dct[s]
    
    row ='INSERT INTO six_col (id_1, form_1, left, right, num, id_2) VALUES (%d, \'%s\', \'%s\', \'%s\', %d, %d);'

    print(row % (id_1, form_1, left, right, num, id_2), file = fout_1)
fout_2.close()

fout_2 = open('output_sql_2.txt', 'r', encoding = 'UTF-8')

for line in fout_2:
    print(line, end = '', file = fout_1)

fout_2.close()
fin.close()
fout_1.close()
