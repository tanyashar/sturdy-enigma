f = open('D:/Downloads/Genproc.csv', 'r', encoding='UTF-8')

a=[]
k = 0
for line in f:
    b = f.readline()
    c = b.split(' ')
    for i in range[5:len(c)-1]:
        print(i)
    k += 1
    if k > 1:
        break
#print((a[0]))

f.close()


"""
#1. найти кол-во биграммов (массив -> множество)
#2. ищем биграммы в обоих множествах
#3. найти разность и пересечение биграммов

#уникальные словформы в тексте
#есть ли опр слово (быстрее чем с мас)
#пересечение, объед, разн

#есть ли у множеств set общие элементы? (пересекаются ли они?)
s1 = set([1, 3, 28, 19])
s = {7, 3, 19, 0, -3}

s | s1 #объединение множеств
s & s1 #пересечение множеств
s1 - s #разность - слова, к-е есть в одном множестве, но их нет в другом
s1 ^ s #все, что вне пересечения

#unix-время. начало эры(с 1янв 1970года)
time.time()
"""

f1 = open('D:/Downloads/Genproc.csv', 'r')
f2 = open('D:/Downloads/skolkovo_ru.csv', 'r')

print(f1.read())

f1.close()
f2.close()
