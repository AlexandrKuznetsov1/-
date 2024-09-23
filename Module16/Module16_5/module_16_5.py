# -*- coding: utf-8 -*-

# Домашнее задание по теме "Шаблонизатор Jinja 2."

# Цель: научиться взаимодействовать с шаблонами Jinja 2 и использовать их в запросах.
#
# Задача "Список пользователей в шаблоне":
# Подготовка:
# Используйте код из предыдущей задачи.
# Скачайте заготовленные шаблоны для их дополнения.
# Шаблоны оставьте в папке templates у себя в проекте.
# Создайте объект Jinja2Templates, указав в качестве папки шаблонов - templates.
# Измените и дополните ранее описанные CRUD запросы:
# Напишите новый запрос по маршруту '/':
# Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html',
# а также передавать в него request и список users.
# Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
# Измените get запрос по маршруту '/users' на '/users/{user_id}':
# Функция по этому запросу теперь принимает аргумент request и user_id.
# Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html',
# а также передавать в него request и одного из пользователей - user.
# Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
# Создайте несколько пользователей при помощи post запроса со следующими данными:
# username - UrbanUser, age - 24
# username - UrbanTest, age - 22
# username - Capybara, age - 60

from fastapi import FastAPI, status, Body, HTTPException, Path, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import List, Annotated
from fastapi.templating import Jinja2Templates

app = FastAPI()
users = []
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except:
        HTTPException(status_code=404, detail="User was not found")


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                  example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", exemple='24')]) -> str:
    if len(users) == 0:
        user_id = 1
    user_id = len(users) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return users[user_id]


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", exemple='24')],
                      user_id: int = Path(ge=1, le=100, description="Enter User ID", example='16')) -> str:
    for edit_user in users:
        if edit_user.id == user_id:
            edit_user.username = username
            edit_user.age = age
            return f"The user {user_id} is updated."
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=0)) -> str:
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users.pop(index)
            return f"User ID {user_id} has been deleted."
    raise HTTPException(status_code=404, detail="User was not found")
