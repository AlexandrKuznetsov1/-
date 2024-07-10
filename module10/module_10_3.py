# -*- coding: utf-8 -*-

# Цель задания:
# Практически применить знания о механизмах блокировки потоков в Python, используя класс Lock из модуля threading.
#
# Задание:
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
#
# Класс BankAccount должен отражать банковский счет с балансом
# и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки,
# чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.

from threading import Thread, Lock
import threading

bunker = Lock()
bunker1 = Lock()


class BankAccount(Thread):

    def __init__(self):
        super().__init__()
        self.bank_account = 1000

    def deposit(self, amount):
        with bunker:
            self.bank_account = self.bank_account + amount
            print(f'Deposited {amount}, new balance is {self.bank_account}')

    def withdraw(self, amount):
        with bunker1:
            self.bank_account = self.bank_account - amount
            print(f'Withdrew {amount}, new balance is {self.bank_account}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()


deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
