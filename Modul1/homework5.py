my_list = ['laptop', 'mouse', 'keyboard', 'screen', 'computer', 'program']
print(my_list)
str = (len(my_list))
print(str)# узнаем количество элементов в списке, для получения шага для вывода (в данном случае 6-1=5)
print(my_list[0::5])
print(my_list[2:5])
my_list[3] = "newkeyboard"
print(my_list)
my_dict = {'laptop':'ноутбук', 'mouse':'мышь', 'keyboard':'клавиатура', 'screen':'экран', 'computer':'компьютер', 'program':'программа'}
print(my_dict)
print(my_dict['mouse'])
my_dict.update({'mouse':'компьютерная мышь'})
print(my_dict)

