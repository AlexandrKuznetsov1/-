# -*- coding: utf-8 -*-

# Цель: научится создавать Inline клавиатуры и кнопки на них в Telegram-bot.
#
# Задача "Ещё больше выбора":
# Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
# Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
# С текстом 'Рассчитать норму калорий' и callback_data='calories'
# С текстом 'Формулы расчёта' и callback_data='formulas'
# Создайте новую функцию main_menu(message), которая:
# Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
# Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
# Создайте новую функцию get_formulas(call), которая:
# Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
# Будет присылать сообщение с формулой Миффлина-Сан Жеора.
# Измените функцию set_age и декоратор для неё:
# Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
# Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.

# По итогу получится следующий алгоритм:
# Вводится команда /start
# На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
# В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
# По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
# По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb3 = InlineKeyboardMarkup()
button_hi = KeyboardButton('/start 👋')
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
in_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
in_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb1.row(button1, button2)
kb2.add(button_hi)
kb3.row(in_button1, in_button2)


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


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("Женская формула: 10 х вес + 6,25 х рост – 5 х возраст – 161"
                              '\n' "Мужская формула: 10 х вес + 6,25 х рост – 5 х года + 5")
    await call.answer

@dp.callback_query_handler(text='calories')
async def set_gender(call):
    await call.message.answer('Введите свой пол муж/жен:')
    await UserState.gender.set()
    await call.answer


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
    if data['gender'] == "жен":
        calorie_allowance = ((10 * int(data['weight'])) + (6.25 * int(data['growth'])) - (4.92 * int(data['age'])) - 161)
    await message.answer(f'Ваша норма калорий {calorie_allowance}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.reply("'Привет! Я бот помогающий твоему здоровью.'", reply_markup=kb2)
    await message.answer('Нажмите на start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)