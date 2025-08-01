from fastapi import FastAPI
from http import HTTPStatus

from fast_zero.schemas import Message, UserSchema, UserPublic, UserDB


app = FastAPI(title='EM FastApi - Curso')

database = [
    # {
    #   "username": "Deus",
    #   "email": "Deus@Deus.com",
    #   "password": "Obrigado",
    #   "id": 1
    # },
    # {
    #   "username": "Rui",
    #   "email": "rui@rui.com",
    #   "password": "ruimano",
    #   "id": 2
    # },
    # {
    #   "username": "Duarte",
    #   "email": "duarte@duarte.com",
    #   "password": "duartemano",
    #   "id": 3
    # }
]


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}


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

