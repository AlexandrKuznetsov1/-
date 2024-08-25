# -*- coding: utf-8 -*-

# Задача "Регистрация покупателей":
# Подготовка:
# Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.
#
# Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
# initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число (не пустой)
# balance - целое число (не пустой)
# add_user(username, email, age), которая принимает: имя пользователя, почту и возраст.
# Данная функция должна добавлять в таблицу Users вашей БД запись с переданными данными.
# Баланс у новых пользователей всегда равен 1000. Для добавления записей в таблице используйте SQL запрос.
# is_included(username) принимает имя пользователя и возвращает True, если такой пользователь есть в таблице Users,
# в противном случае False. Для получения записей используйте SQL запрос.
#
# Изменения в Telegram-бот:
# Кнопки главного меню дополните кнопкой "Регистрация".
# Напишите новый класс состояний RegistrationState со следующими объектами класса State:
# username, email, age, balance(по умолчанию 1000).
# Создайте цепочку изменений состояний RegistrationState.
# Функции цепочки состояний RegistrationState:
# sing_up(message):
# Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
# Эта функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
# После ожидать ввода возраста в атрибут RegistrationState.username при помощи метода set.
# set_username(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
# Функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
# Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username на message.text.
# Далее выводится сообщение "Введите свой email:" и принимается новое состояние RegistrationState.email.
# Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует,
# введите другое имя" и запрашивать новое состояние для RegistrationState.username.
# set_email(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
# Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
# Далее выводить сообщение "Введите свой возраст:":
# После ожидать ввода возраста в атрибут RegistrationState.age.
# set_age(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
# Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
# Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users
# при помощи ранее написанной crud-функции add_user.
# В конце завершать приём состояний при помощи метода finish().
# Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
from PIL import Image
import crud_functions


api = "6999041846:AAFqIodeNkSD_lFv1DjzoO1G3TZ1gahVygM"
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
button4 = KeyboardButton(text='Регистрация')

in_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
in_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
in_button3 = InlineKeyboardButton(text="Product1", callback_data="product_buying")
in_button4 = InlineKeyboardButton(text="Product2", callback_data="product_buying")
in_button5 = InlineKeyboardButton(text="Product3", callback_data="product_buying")
in_button6 = InlineKeyboardButton(text="Product4", callback_data="product_buying")

# Привязка кнопок
kb1.add(button4)
kb1.row(button1, button2, button3)
kb2.add(button_hi)
kb3.row(in_button1, in_button2)
kb4.add(in_button3, in_button4, in_button5, in_button6)


class UserState(StatesGroup):
    gender = State()  # пол
    age = State()  # возраст
    growth = State()  # рост
    weight = State()  # вес


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Нажмите 'Регистрация'", reply_markup=kb1)


@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    # await message.answer("Введите имя пользователя (только латинский алфавит):")

    if crud_functions.is_included(message.text) != True:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    if crud_functions.is_included(message.text) == True:
        await message.answer("Пользователь существует, введите другое имя")
        await message.answer("Введите имя пользователя (только латинский алфавит):")
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    crud_functions.add_user(data['username'], data['email'], data['age'])
    print(data)
    await state.finish()


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