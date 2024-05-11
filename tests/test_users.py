from http import HTTPStatus

from fast_zero.schemas import UserPublic


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
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users')

    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'Test_User',
            'email': 'test_user@email.com',
            'password': 'new_123456',
        },
    )  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'username': 'Test_User',
        'email': 'test_user@email.com',
        'id': user.id,
    }


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}', headers={'Authorization': f'Bearer {token}'}
    )  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'User deleted'}


def test_read_one_user(client, user):
    response = client.get('/users/1')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'username': 'Test_User',
        'email': 'test_user@email.com',
        'id': 1,
    }


def test_read_user_not_found(client, user):
    response = client.get('/users/2')  # Act

    assert response.status_code == HTTPStatus.NOT_FOUND  # Assert
    assert response.json() == {'detail': 'User not found'}


def test_duplicated_user(client, user):
    response = client.post(
        '/users',
        json={
            'username': 'Test_User',
            'email': 'test_user@email.com',
            'password': '123456',
        },
    )  # Act

    assert response.status_code == HTTPStatus.BAD_REQUEST  # Assert
    assert response.json() == {'detail': 'Username already registered'}
