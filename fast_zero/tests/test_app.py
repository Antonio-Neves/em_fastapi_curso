from http import HTTPStatus


def test_root_deve_retornar_hello_world(client):

    response = client.get('/')

    assert response.json() == {'message': 'Hello World!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'rui',
            'email': 'rui@rui.com',
            'password': 'ruipassword'
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 4,
        'username': 'rui',
        'email': 'rui@rui.com'
    }


def test_read_users(client):

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                "username": "Deus",
                "email": "deus@deus.com",
                # "password": "Obrigado",
                "id": 1
            },
            {
                "username": "Rui",
                "email": "rui@rui.com",
                # "password": "ruimano",
                "id": 2
            },
            {
                "username": "Duarte",
                "email": "duarte@duarte.com",
                # "password": "duartemano",
                "id": 3
            },
            {
                "username": "rui",
                "email": "rui@rui.com",
                # "password": "duartemano",
                "id": 4
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Manuel',
            'emali': 'manuel@manuel.com',
            'pasaword': 'senha'
        }
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Manuel',
        'email': 'manuel@manuel.com',
        'id': 1,
    }


def test_delete_user(clien):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Manuel',
        'email': 'manuel@manuel.com',
        'id': 1,
    }
