import pytest
from flask import session

def test_register(client):
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200
    response = client.post(
        '/authentication/register', 
        data={'user_name': 'user4', 'password':'User4_password'}
    )

@pytest.mark.parametrize(('user_name', 'password', 'message'),(
        ('cj', 'TestPassword1', b'Your user name is too short'),
        ('user_1', 'Test1234', b'Your user name is already taken - please supply another')
))

def test_register_with_invalid(client, user_name, password, message):
    response = client.post(
        '/authentication/register', 
        data={'user_name': user_name, 'password': password}
    )
    assert message in response.data

def test_logout(client, auth):
    auth.login()
    with client:
        auth.logout()
        assert 'user_id' not in session

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200