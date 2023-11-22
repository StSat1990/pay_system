from fastapi import APIRouter
from datetime import datetime

from database.userservice import (register_user_db, edit_user_db, delete_user_db,
                                  get_exact_user_db, chek_user_email_db)

from user import UserRegisterValidator, EditUserValidator

user_router = APIRouter(prefix='/user', tags=['Работа с пользователем'])

#Регистрация пользователя
@user_router.post('/register')
async def register_user(data: UserRegisterValidator):
    #Переводим из типа pydantic в обычный словарь
    new_user_data = data.model_dump()

    #Вызов функции для проверки почты в базе
    checker = chek_user_email_db(data.email)

    #Если нет в базе такого email пользователя, то добавляем
    if not checker:
        result = register_user_db(reg_date=datetime.now(), **new_user_data)
        return {'message': result}
    else:
        return {'message': 'Пользователь с таким email уже существут'}

#Получение информации о пользователе
@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нет такого пользователя'}

#Изменить данные пользователя
@user_router.put('/edit-data')
async def edit_user(data: EditUserValidator):
    #Переводим из pydantic в простой словарь
    change_data = data.model_dump()

    result = edit_user_db(**change_data)

    return {'message': result}

#Удаление пользователя
@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    if result:
        return {'message': 'Пользователь успешно удален'}
    else:
        return {'message': 'Такого пользователя не существует'}



