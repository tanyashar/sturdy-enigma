import urllib.request
import re
#url = 'https://yandex.ru/pogoda/moscow'
url = 'https://habrahabr.ru/'
user_a = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
req = urllib.request.Request(url, headers={'User-Agent':user_a})
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')
#print(html[:200])

regPostTitle = re.compile('<h2 class="post__title">.*?</h2>', flags = re.U | re.DOTALL)
titles = regPostTitle.findall(html)
#print(len(titles))
print(titles[:2])

newTitles = []
regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL)
#все, кроме пробельных символов, повторяющееся 2 и больше раз
for t in titles:
    clean_t = regSpace.sub("", t)
    #куда_записываем = что_удаляем.какой_функцией(на_что_меняем, откуда_удаляем)
    #print(clean_t)
    clean_t = regTag.sub("", clean_t)
    newTitles.append(clean_t)
    #print(clean_t, '\n')
  
for t in newTitles: 
    print(t.replace("&nbsp;&rarr;", " -> "))


