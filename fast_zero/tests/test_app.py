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
        'id': 1,
        'username': 'rui',
        'email': 'rui@rui.com'
    }


def test_read_users(client):

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'rui',
                'email': 'rui@rui.com'
            }
        ]
    }
