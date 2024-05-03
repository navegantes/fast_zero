from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)  # Arrange


def test_root_deve_retornar_ok_e_ola_mundo():
    # client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_html_message_ola_mundo():
    # client = TestClient(app)  # Arrange

    response = client.get('/helloworld')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.text == """<h1>Olá Mundo!</h1>"""  # Assert
