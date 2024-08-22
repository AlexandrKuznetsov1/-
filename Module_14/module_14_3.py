# -*- coding: utf-8 -*-

# Цель: подготовить Telegram-бота для взаимодействия с базой данных.
#
# Задача "Витамины для всех!":
# Подготовка:
# Подготовьте Telegram-бота из последнего домашнего задания 13 моудля сохранив код с ним в файл module_14_3.py.
# Если вы не решали новые задания из предыдущего модуля рекомендуется выполнить их.
#
# Дополните ранее написанный код для Telegram-бота:
# Создайте и дополните клавиатуры:
# В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
# Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4".
# У всех кнопок назначьте callback_data="product_buying"
# Создайте хэндлеры и функции к ним:
# Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
# Функция get_buying_list должна выводить надписи:
# 'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза.
# После каждой надписи выводите картинки к продуктам.
# В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".

# Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
# Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
from PIL import Image


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Клавиатуры
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb3 = InlineKeyboardMarkup()
kb4 = InlineKeyboardMarkup()

# Кнопки
button_hi = KeyboardButton('/start 👋')

button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')

in_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
in_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
in_button3 = InlineKeyboardButton(text="Product1", callback_data="product_buying")
in_button4 = InlineKeyboardButton(text="Product2", callback_data="product_buying")
in_button5 = InlineKeyboardButton(text="Product3", callback_data="product_buying")
in_button6 = InlineKeyboardButton(text="Product4", callback_data="product_buying")

# Привязка кнопок
kb1.row(button1, button2, button3)
kb2.add(button_hi)
kb3.row(in_button1, in_button2)
kb4.add(in_button3, in_button4, in_button5, in_button6)

# создаем список фото
dict_foto_ = {"Drinks_Hamburger.jpg": 'Гамбургер - 970 кал.', "Butterbrot.jpg": 'Бутерброд - 1500 кал.',
              "Fast_food_Pizza.jpg": 'Пицца - 1790 кал.', "Fast_food_Hot_dog.jpg": 'Хот-дог - 2440 кал.'}

class UserState(StatesGroup):
    gender = State()  # пол
    age = State()  # возраст
    growth = State()  # рост
    weight = State()  # вес

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Нажмите 'Рассчитать'", reply_markup=kb1)

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb3)

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i, j, k in zip(range(1, 5), dict_foto_, dict_foto_.values()):
        await message.answer(f"Название: Product{i} | Описание: {k} | Цена: {i * 100}")
        with open(f'foto/{j}', 'rb') as img:
            await message.answer_photo(photo=img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb4)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("Женская формула: 10 х вес + 6,25 х рост – 5 х возраст – 161"
                              '\n' "Мужская формула: 10 х вес + 6,25 х рост – 5 х года + 5")
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_gender(call):
    await call.message.answer('Введите свой пол муж/жен:')
    await UserState.gender.set()
    await call.answer()

@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    await state.update_data(gender=message.text)
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    if data['gender'] == "муж":
        calorie_allowance = ((10 * int(data['weight'])) + (6.25 * int(data['growth'])) - (4.92 * int(data['age'])) + 5)
    elif data['gender'] == "жен":
        calorie_allowance = ((10 * int(data['weight'])) + (6.25 * int(data['growth'])) - (4.92 * int(data['age'])) - 161)
    await message.answer(f'Ваша норма калорий {calorie_allowance}')
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.reply("'Привет! Я бот помогающий твоему здоровью.'", reply_markup=kb2)
    await message.answer('Нажмите на start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)