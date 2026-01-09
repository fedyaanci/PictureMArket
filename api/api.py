from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

from Schemas.User import UserLoginSchema
app = FastAPI()

users = [{'id': 1, 'name': 'fedya', 'age' : 20, 'depression': True},
         {'id': 2,'name': 'petya', 'age' : 24, 'depression': False}]

@app.get('/users', tags=['Users'], summary='Получить всех пользователей')
def GetUsers():
    return users

@app.get('/users/{user_id}',tags=['Users'], summary='Получить конкретного пользователя')
def GetUser(user_id: int):
    for user in users:
        if user['id'] == user_id: 
            return user  
    raise HTTPException(status_code=404, detail= {'message': 'user is not exist'})

@app.post('/users')
def AddUser(new_user: UserLoginSchema):
    users.append({
        'id': len(users)+1,
        'name': new_user.name,
        'age': new_user.age,
        'depression' : new_user.depression
    })
    return users[-1]
    