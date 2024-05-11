from http import HTTPStatus

from jwt import decode

from fast_zero.security import Settings

settings = Settings()


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token


def test_credential_exception(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': 'Bearer INVALID-TOKEN'},
        data={'username': 'Invalid_User', 'email': 'test_user@email.com'},
    )

    resp = response.json()
    payload = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )
    username: str = payload.get('sub')

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert username not in resp
