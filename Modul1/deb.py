date_ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
month_ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
list_zodiac = ('Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces')
elements_ = ('Fire', 'Earth', 'Air', 'Water')
element_fire = ('You are a passionate, active, energetic person. '
                'You have a strong character and strive for leadership')
element_earth = ("You are a practical, hardworking, stubborn and sensible person. "
                 "Love stability and reliability, and also takes care of material things.")
element_air = ('You are a sociable, intelligent person, with logical thinking and the ability to communicate '
               'with people. You prefer reason and analysis, and also strive for new knowledge and ideas.')
element_water = ('You are a sensitive, intuitive and emotional person. You have the ability to empathize '
                 'and emotionally understand other people.')
horoscope = ('Luck awaits you at work', 'Success awaits you in family affairs', 'You can win the lottery',
                  "It's time for you to think about your loved ones", "Today it's useful to walk in the park",
                  'You will make a pleasant acquaintance', 'material well-being awaits you',
                  'Today you better relax', 'Beware of scammers', 'A day of unity with nature',
                  'A wonderful day to go to the theater', 'The best day for sports',
                  'Your superiors will celebrate your labors', 'The advice of your loved ones will help',
                  'you get out of a difficult situation', 'a romantic evening awaits you')
name = input('Enter You name : ')
c = len(name)
while c != 0 :
    in_date = input('Enter the day of your birth : ')
    in_moth = input('Enter the month of your birth : ')
    a = int(in_date)
    b = int(in_moth)
    if a > 29 and b == 2 or a > 30 and b == 4 or a > 30 and b == 6 or a > 30 and b == 9 or a > 30 and b == 11 :
        print('Sorry, you entered incorrect data.')
    if a in date_ and b in month_:
        c = 0
print("Hello", str(name), 'your a patron :')
if a >= 21 and b == 3 or a <= 20 and b == 4 :
    print(list_zodiac[0])
    print('Yuor element :', elements_[0], ":", element_fire)
if a >= 21 and b == 4 or a <= 21 and b == 5 :
    print(list_zodiac[:1])
    print('Yuor element :', elements_[1], ":", element_earth)
if a >= 22 and b == 5 or a <= 21 and b == 6 :
    print(list_zodiac[2])
    print('Yuor element :', elements_[2], ":", element_air)
if a >= 22 and b == 6 or a <= 22 and b == 7 :
    print(list_zodiac[3])
    print('Yuor element :', elements_[3], ":", element_water)
if a >= 23 and b == 7 or a <= 21 and b == 8 :
    print(list_zodiac[4])
    print('Yuor element :', elements_[0], ":", element_fire)
if a >= 22 and b == 8 or a <= 23 and b == 9 :
    print(list_zodiac[5])
    print('Yuor element :', elements_[1], ":", element_earth)
if a >= 24 and b == 9 or a <= 23 and b == 10 :
    print(list_zodiac[6])
    print('Yuor element :', elements_[2], ":", element_air)
if a >= 24 and b == 10 or a <= 22 and b == 11 :
    print(list_zodiac[7])
    print('Yuor element :', elements_[3], ":", element_water)
if a >= 23 and b == 11 or a <= 22 and b == 12 :
    print(list_zodiac[8])
    print('Yuor element :', elements_[0], ":", element_fire)
if a >= 23 and b == 12 or a <= 20 and b == 1 :
    print(list_zodiac[9])
    print('Yuor element :', elements_[1], ":", element_earth)
if a >= 21 and b == 1 or a <= 19 and b == 2 :
    print(list_zodiac[10])
    print('Yuor element :', elements_[2], ":", element_air)
if a >= 20 and b == 2 or a <= 20 and b == 3 :
    print(list_zodiac[11])
    print('Yuor element :', elements_[3], ":", element_water)
print ('Your horoscope for today : ')
import random
d = random.choice(horoscope)
print(d)
# В ЭТОМ МЕСТЕ НЕОБХОДИМО ОБНОВЛЕНИЕ СПИСКА ГОРОСКОП ОТ ПОЛЬЗОВАТЕЛЯ С СОХРАНЕНИЕМ ДАННЫХ
# В КОДЕ ЭТО НЕВОЗМОЖНО ОСУЩЕСТВИТЬ, ИЗУЧАЮ ДОБАВЛЕНИЕ ФАЙЛА)))))))
#import time
#print("Leave a forecast for someone please")
#time.sleep(5)
#print('But remember, he can come back to you')
#time.sleep(5)
#prediction = [input(str("Go :"))]
#w = str(prediction)
#f w in horoscope :
    #print('Thank you, Good buy !')
#horoscope.append(w)
#print("Thank you for the development !")
#print(horoscope)

