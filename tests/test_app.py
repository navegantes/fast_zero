from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_html_message_ola_mundo(client):
    response = client.get('/helloworld')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.text == """<h1>Olá Mundo!</h1>"""  # Assert


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'Test User',
            'email': 'test@email.com',
            'password': '123456',
        },
    )  # Act

    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        'username': 'Test User',
        'email': 'test@email.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'users': [
            {
                'username': 'Test User',
                'email': 'test@email.com',
                'id': 1,
            }
        ]
    }


def test_read_one_user(client):
    response = client.get('/users/1')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'username': 'Test User',
        'email': 'test@email.com',
        'id': 1,
    }


def test_read_invalid_user(client):
    response = client.get('/users/0')  # Act

    assert response.status_code == HTTPStatus.NOT_FOUND  # Assert
    assert response.json() == {"detail": "User not found"}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Test User',
            'email': 'test@email.com',
            'password': 'new_123456',
        },
    )  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'username': 'Test User',
        'email': 'test@email.com',
        'id': 1,
    }


def test_update_invalid_user(client):
    response = client.put(
        '/users/0',
        json={
            'username': 'Test User',
            'email': 'test@email.com',
            'password': 'new_123456',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_delete_user(client):
    response = client.delete('/users/1')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'User deleted'}


def test_delete_invalid_user(client):
    response = client.delete('/users/0')  # Act

    assert response.status_code == HTTPStatus.NOT_FOUND  # Assert
    assert response.json() == {"detail": "User not found"}
