grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
 # узнаем количество учеников
x = len(students) # 5 учеников
 # проверяем всем ли выставлены оценки
y = len(grades) # 5
if x == y : #если значения соответсвуют, то
    name_students = sorted(students) # сортируем учеников в алфавитном порядке т.к. grades для каждого ученика в алфавитном порядке
 # создаем списки оценок для каждого ученика
new_grades = []
for i in  grades :
    a = list(i)
    new_grades.append(a)
res1 = new_grades[0]
res2 = new_grades[1]
res3 = new_grades[2]
res4 = new_grades[3]
res5 = new_grades[4]
 # т.к. пробелы учитываются как отдельные (нечетные) элементы списка удаляем их:
new_res1 = res1[0::2]
new_res2 = res2[0::2]
new_res3 = res3[0::2]
new_res4 = res4[0::2]
new_res5 = res5[0::2]
 # преобразовываем строчные значения в числовые, средний балл не будет целым числом, по этому сразу Float
itog_ball = []
ball1 = []
for k in new_res1 :
    c = float(k)
    ball1.append(c)
b = sum(ball1) / len(ball1)
itog_ball.append(b)
ball2 = []
for k in new_res2 :
    c = float(k)
    ball2.append(c)
b2 = sum(ball2) / len(ball2)
itog_ball.append(b2)
ball3 = []
for k in new_res3 :
    c = float(k)
    ball3.append(c)
b3 = sum(ball3) / len(ball3)
itog_ball.append(b3)
ball4 = []
for k in new_res4 :
    c = float(k)
    ball4.append(c)
b4 = sum(ball4) / len(ball4)
itog_ball.append(b4)
ball5 = []
for k in new_res5 :
    c = float(k)
    ball5.append(c)
b5 = sum(ball5) / len(ball5)
itog_ball.append(b5)
 # создаем словарь с итоговым результатом:
dict_ = {}
keys = name_students
values = itog_ball
 # т.к. списки keys и values уже упоорядочены добавляем их в словарь
dict_.update({keys[0]:values[0]})
dict_.update({keys[1]:values[1]})
dict_.update({keys[2]:values[2]})
dict_.update({keys[3]:values[3]})
dict_.update({keys[4]:values[4]})


print(dict_)

