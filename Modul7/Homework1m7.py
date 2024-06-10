# -*- coding: utf-8 -*-
# Задание
# Создать в директории проекта текстовый файл с расширением txt
# Добавить в этот файл текст,- стихотворение Байрона
# Создать переменную с этим файлом
# Распечатать содержимое текстового файла в консоль
# Закрыть файл

file_name = 'Byron.txt'  # Создаем в директории проекта текстовый файл с расширением txt
file = open(file_name, mode='w', encoding='utf-8')
file_content = '# -*- coding: utf-8 -*-'
file.write(file_content + '\n')
file.close()
text_to_add = 'My soul is dark - Oh! quickly string'  # Добавляем в этот файл текст,- стихотворение Байрона
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'The harp I yet can brook to hear;'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'And let thy gentle fingers fling'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = "Its melting murmurs o'er mine ear."
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'If in this heart a hope be dear,'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'That sound shall charm it forth again:'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'If in these eyes there lurk a tear,'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'Twill flow, and cease to burn my brain.'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = ""
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'But bid the strain be wild and deep,'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'Nor let thy notes of joy be first:'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'I tell thee, minstrel, I must weep,'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'Or else this heavy heart will burst;'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'For it hath been by sorrow nursed,'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'And ached in sleepless silence, long;'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = "And now 'tis doomed to know the worst,'"
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')
text_to_add = 'And break at once - or yield to song.'
with open('Byron.txt', 'a') as file:
    file.write(text_to_add + '\n')

byron = r"C:\Users\Александр\Homeworks\Modul7\Byron.txt"  # Создаем переменную с этим файлом
with open('Byron.txt', 'r') as file:
    text = " ".join(line.rstrip() for line in file)
    print(text)  # Распечатываем содержимое текстового файла в консоль
file.close()  # Закрыть файл
