# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Дело было так:
# Коварные гоблины захватили деревню гномов и каждый месяц отправляют по 3 гнома в шахту.
# Гномы работают без выходных (жаль бедолаг) но когда они берут лишний груз они садятся в углу
# пещеры и отдыхают, чем тяжелей была ноша,- тем больше времени на отдых. Перерыв на обед 1 час
# Так как гоблины не умеют считать, в конце недели они попросили нарисовать насколько эффективно работают гномы.
#
# Цель: визуализировать результаты работы бедных гномов


class Dwarf:
    def __init__(self, *args):
        self.list_name = args
        self.work = []
        self.time = []
        self.work_time_dwarf1_ = {}
        self.work_time_dwarf2_ = {}
        self.work_time_dwarf3_ = {}
        for i in self.list_name:
            self.dwarf1 = str(i[0])
            self.dwarf2 = str(i[1])
            self.dwarf3 = str(i[2])
            for j in i:
                Dwarf.work(self, name=j)

    def work(self, name):
        day = 0
        while day < 7:
            time_start = time.time()
            cargo = random.randint(10, 1000)
            time.sleep(0.1)  # симулируем время обеда
            if cargo <= 350:
                time.sleep(0.1)  # симулируем время перекура
            if cargo > 350 <= 700:
                time.sleep(0.2)
            if cargo > 700 <= 1000:
                time.sleep(0.3)
            time_end = time.time()
            time_rest = round((time_end - time_start), 1)
            if name in self.dwarf1:
                self.work_time_dwarf1_[cargo] = time_rest

            if name in self.dwarf2:
                self.work_time_dwarf2_[cargo] = time_rest

            if name in self.dwarf3:
                self.work_time_dwarf3_[cargo] = time_rest
            day += 1
            if self.work_time_dwarf1_:
                if self.work_time_dwarf2_:
                    if len(self.work_time_dwarf3_) == 7:
                        ax1 = plt.subplots()
                        plt.plot(self.work_time_dwarf1_.keys(), label=self.dwarf1)
                        plt.plot(self.work_time_dwarf2_.keys(), label=self.dwarf2)
                        plt.plot(self.work_time_dwarf3_.keys(), label=self.dwarf3)
                        plt.legend(loc='best')
                        plt.xlabel('дни', fontsize=14)
                        plt.ylabel('вес груза', fontsize=14)
                        plt.xlim(-1, 7)
                        plt.title(r' График нагрузки', fontsize=16)
                        # time.sleep(0.3)
                        ax2 = plt.subplots()
                        plt.plot(self.work_time_dwarf1_.values(), label=self.dwarf1)
                        plt.plot(self.work_time_dwarf2_.values(), label=self.dwarf2)
                        plt.plot(self.work_time_dwarf3_.values(), label=self.dwarf3)
                        plt.legend(loc='best')
                        plt.xlabel('дни', fontsize=14)
                        plt.ylabel('время отдыха', fontsize=14)
                        plt.xlim(-1, 7)
                        plt.title(r' График отдыха', fontsize=16)
                        # time.sleep(0.3)
                        wd1 = []
                        td1 = []
                        for i, j in self.work_time_dwarf1_.items():
                            wd1.append(i)
                            td1.append(j)
                        wd2 = []
                        td2 = []
                        for i, j in self.work_time_dwarf2_.items():
                            wd2.append(i)
                            td2.append(j)
                        wd3 = []
                        td3 = []
                        for i, j in self.work_time_dwarf3_.items():
                            wd3.append(i)
                            td3.append(j)

                        wd = [wd1, wd2, wd3]
                        td = [td1, td2, td3]
                        print(f'Создаем массив чисел с результатами работы гномов за неделю "wd =" {wd}')
                        time.sleep(0.3)
                        print(f'Создаем массив чисел с результатами отдыха гномов за неделю "td =" {td}')
                        time.sleep(0.3)

                        sum_wd = sum(map(np.array, wd))
                        sum_time = sum(map(np.array, td))
                        print(f'Обрабатываем массив с помощью "sum(map(np.array, wd))" и получаем общий результат'
                              f' за неделю "sum_wd =" {sum_wd}')
                        time.sleep(0.3)
                        print(f'Обрабатываем массив с помощью "sum(map(np.array, td))" и получаем общий результат'
                              f' за неделю "sum_time =" {sum_time}')

                        ax3 = plt.subplots()
                        plt.plot(sum_wd, label='Все вместе принесли')
                        plt.legend(loc='best')
                        plt.xlabel('дни', fontsize=14)
                        plt.ylabel('общий вес груза', fontsize=14)
                        plt.xlim(-1, 7)
                        plt.title(r' Общий график нагрузки', fontsize=16)
                        # time.sleep(0.3)

                        ax4 = plt.subplots()
                        plt.plot(sum_time, label='Все вместе отдохнули')
                        plt.legend(loc='best')
                        plt.xlabel('дни', fontsize=14)
                        plt.ylabel('общее время отдыха', fontsize=14)
                        plt.xlim(-1, 7)
                        plt.title(r' Общий график отдыха', fontsize=16)

                        plt.show()


list_name = ['alex', 'bob', 'jack']
dwarf = Dwarf(list_name)
