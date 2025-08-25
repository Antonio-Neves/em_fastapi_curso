from fastapi import FastAPI, HTTPException
from http import HTTPStatus

from fast_zero.schemas import Message, UserSchema, UserPublic, UserDB, UserList


app = FastAPI(title='EM FastApi - Curso')

database = [
    {
      "username": "Deus",
      "email": "deus@deus.com",
      "password": "Obrigado",
      "id": 1
    },
    {
      "username": "Rui",
      "email": "rui@rui.com",
      "password": "ruimano",
      "id": 2
    },
    {
      "username": "Duarte",
      "email": "duarte@duarte.com",
      "password": "duartemano",
      "id": 3
    }
]


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():

    return {'message': 'Hello World!'}


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():

    return {'users': database}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):

    user_with_id = UserDB(
        # username=user.username,
        # email=user.email,
        # password=user.password,
        **user.model_dump(), # Unpack and transform again in a dict with model_dump
        id=len(database) + 1
    )

    database.append(user_with_id)

    return user_with_id


@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):

    user_with_id = UserDB(**user.model_dump(), id=user_id)

    if user_id < 1 or user_id > len(database):

        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Not found!'
        )

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):

    if user_id < 1 or user_id > len(database):

        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Not found!'
        )

    return database.pop(user_id - 1)

