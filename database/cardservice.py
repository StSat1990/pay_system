# в user __init__.py
# Прописать валидацию

from database.models import UserCard
from database import get_db

def add_card_db(user_id, card_number, balance, card_name, exp_date):
    db = next(get_db())

    new_card = UserCard(user_id=user_id, card_number=card_number, balance=balance,
                        card_name=card_name, exp_date=exp_date)

    db.add(new_card)
    db.commit()

    return 'Карта успешно добавлена'

# Вывести все карты определенного пользователя через user_id
def exact_user_card_db(user_id):
    db = next(get_db())

    checker = db.query(UserCard).filter_by(user_id=user_id).all()

    return checker

# Вывести определенную карту определенного пользователя
def get_card_db(user_id, card_id):
    db = next(get_db())

    checker = db.query(UserCard).filter_by(user_id=user_id, card_id=card_id).first()

    return checker

def check_card_db(card_number):
    db = next(get_db())

    checker = db.query(UserCard).filter_by(card_number=card_number).first()

    return checker

def delete_card_db(card_id):
    db = next(get_db())

    delete_card = db.query(UserCard).filter_by(card_id=card_id).first()

    if delete_card:
        db.delete(delete_card)
        db.commit()

        return 'Карта успешно удалена'
    else:
        return 'Карта не найдена'