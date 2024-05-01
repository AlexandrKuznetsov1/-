def test():
    a = 12
    b = 365
    print(a) #параметр а
    print(b) #параметр b
    print(a, b) #параметры а и b
    print(a+b) #сумма параметров a и b
(test())
def test2(a=1, b=2, c=3):
    print(a,b,c)
    print((a + b) * 3) # можно осуществлять действия с параметрами
(test2())
def test3(a, b, c):
    print(a, b, c)
test3('Надеюсь', 'все', 'верно')
import time #закрепляю )))
time.sleep(3)
print('Спасибо!')