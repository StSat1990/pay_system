# Получить все переводы по карте

from datetime import datetime
from database.models import Transfer, UserCard
from database import get_db

#Проверка карты для создание перевода
def validate_card(card_number, db):
    db = next(get_db())

    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card

#Перевод денег
def get_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    #Проверка на наличие в базе обеих карт
    checker_card_from = validate_card(card_from, db)
    checker_card_to = validate_card(card_to, db)

    if checker_card_from and checker_card_to:
        if checker_card_from.balance >= amount:
            checker_card_from.balance -= amount
            checker_card_to.balance += amount

            new_transaction = Transfer(card_from_id=card_from, card_to_id=card_to,
                                       ammount=amount, transaction_date=datetime.now())

            db.add(new_transaction)
            db.commit

            return "Перевод успешно выполнен"

        else:
            return "Не достаточно средств на балансе"

    else:
        return "Одна или обе карты не существуют"

#Получение всех транзакций
def get_card_transaction_db(card_from_id):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()

    return card_transaction

# Отменить перевод
def cancel_transfer_db(card_from, card_to, amount, transfer_id):
    db = next(get_db())
    # Проверка на наличии карты в бд обеих карт
    check_card_from = validate_card(card_from, db)
    check_card_to = validate_card(card_to, db)
    # Если обе карты существуют в бд перевод
    if check_card_from and check_card_to:
        # Проверить баланс того кто возвращает деньги
        if check_card_to.balance >= amount:
            # Отнимаем тому кто получил до этого
            check_card_to.balance -= amount
            # Добавляем у того кто отправил до этого
            check_card_from.balance += amount

            # Сохраняем в базе
            exact_transaction = db.query(Transfer).filter_by(transfer_id=transfer_id).first()
            exact_transaction.status = False

            db.commit()

            return "Перервод успешно отменен"
        else:
            return "Недостаточно средств на балансе"

    return "Одна из карт не существует"