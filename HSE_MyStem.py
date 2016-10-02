import os
inp = "input_texts" #директория
lst = os.listdir(inp) #формирование списка файлов и директорий в папке
for fl in lst:
    os.system(r"C:\mystem.exe " + inp + os.sep + fl + " output_texts" + os.sep + fl)

#os.sep = разделитель пути для конкретной операционной системы (Винда = '\\')
