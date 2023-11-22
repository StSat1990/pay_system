from pydantic import BaseModel

class CardAddValidator(BaseModel):
    user_id: int
    card_number: int
    card_name: str
    balance = float
    ext_date = int