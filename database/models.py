from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#Создание таблицы пользователей
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String,unique=True)
    city = Column(String)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)

#Таблица карт пользователя
class UserCard(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    card_number = Column(Integer, nullable=False)
    balance = Column(Float, default=0)
    ext_date = Column(Integer, nullable=False)
    card_name = Column(String)
    user_fk = relationship(User, lazy='subquery')

#Таблица переводов(Транзакция)
class Transfer(Base):
    __tablename__ = 'transfers'
    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    card_from_id = Column(Integer, ForeignKey("cards.card_id"))
    card_to_id = Column(Integer, ForeignKey("cards.card_id"))
    amount = Column(Float)
    status = Column(Boolean, default=True)
    transaction_date = Column(DateTime)
    card_from_fk = relationship(UserCard, foreign_keys=[card_from_id], lazy='subquery')
    card_to_fk = relationship(UserCard, foreign_keys=[card_from_id], lazy='subquery')
