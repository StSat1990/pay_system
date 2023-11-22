from pydantic import BaseModel

class UserRegisterValidator(BaseModel):
    name: str
    last_name: str
    email: str
    phone_number: str
    password: str
    city: str

class EditUserValidator(BaseModel):
    user_id: str
    edit_type: str
    new_data: str