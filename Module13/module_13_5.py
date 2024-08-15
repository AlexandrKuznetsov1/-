# -*- coding: utf-8 -*-

# Цель: научится создавать клавиатуры и кнопки на них в Telegram-bot.
#
# Задача "Меньше текста, больше кликов":
# Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела
# для расчёта калорий выдавались по нажатию кнопки.
# Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать',
# а не на 'Calories'.
# Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом:
# 'Рассчитать' и 'Информация'. Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства
# при помощи параметра resize_keyboard.
# Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
# В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками.
# При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age
# с которой начинается работа машины состояний для age, growth и weight.


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_hi = KeyboardButton('/start 👋')
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb1.row(button1, button2)
kb2.add(button_hi)


class UserState(StatesGroup):
    gender = State()  # пол
    age = State()  # возраст
    growth = State()  # рост
    weight = State()  # вес


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Нажмите 'Рассчитать'", reply_markup=kb1)


@dp.message_handler(text=['Рассчитать'])
async def set_gender(message):
    await message.answer('расчет по формуле базового обмена веществ Миффлина-Сан Жеора')
    await message.answer('Введите свой пол муж/жен:')
    await UserState.gender.set()


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