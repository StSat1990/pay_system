from datetime import datetime
from database.models import User
from database import get_db

#Регистрация пользователей
def register_user_db(name, surname, email, password, city, phone_number, reg_date):
    db = next(get_db())

    new_user = User(name=name, surname=surname, email=email, password=password,
                    city=city, phone_number=phone_number, reg_date=datetime.now())

    db.add(new_user)
    db.commit()

    return 'Пользователь успешно зарегистрирован'

#Получить информацию об определенном пользоваетеле
def get_exact_user_db(user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(user_id=user_id).first()

    return checker

#Проверка данных через e-mail
def chek_user_email_db(email):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    return checker

#Изменение данных пользователя
def edit_user_db(user_id, edit_type, new_date):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_type == 'mail':
            exact_user.email = new_date

        elif edit_type == 'password':
            exact_user.email = new_date

        elif edit_tpe == 'city':
            exact_user.email = new_date

        db.commit()

        return 'Данные успешно обновлены'
    else:
        return 'Пользователь не найден'

#Удаление пользователя
def delete_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        db.delete(exact_user)
        db.commit()

        return 'Пользователь успешно удален'
    else:
        return 'Пользователь не найден'

