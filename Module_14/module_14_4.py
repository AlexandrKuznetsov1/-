# -*- coding: utf-8 -*-

# Задача "Продуктовая база":
# Подготовка:
# Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.
#
# Дополните ранее написанный код для Telegram-бота:
# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# title(название продукта) - текст (не пустой)
# description(описание) - текст
# price(цена) - целое число (не пустой)
# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
#
# Изменения в Telegram-бот:
# В самом начале запускайте ранее написанную функцию get_all_products.
# Измените функцию get_buying_list в модуле с Telegram-ботом,
# используя вместо обычной нумерации продуктов функцию get_all_products.
# Полученные записи используйте в выводимой надписи: "Название: <title> | Описание: <description> | Цена: <price>"
# Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
from PIL import Image
import crud_functions


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
all_products = crud_functions.get_all_products()
# print(all_products)
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
    for i in all_products:
        await message.answer(f"Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}")
        with open(f'foto/{i[4]}', 'rb') as img:
            await message.answer_photo(photo=img)
    # crud_functions.connection.close()
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