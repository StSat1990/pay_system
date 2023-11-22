from fastapi import FastAPI

from user.user_api import user_router

app = FastAPI(docs_url='/')

app.include_router(user_router)

@app.get('/nome')
async def home():
    return {'message': 'hello this is home'}
