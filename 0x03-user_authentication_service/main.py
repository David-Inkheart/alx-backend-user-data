#!/usr/bin/env python3
"""
End-to-end integration test
"""

import requests


def register_user(email: str, password: str) -> None:
    """Test for register_user"""
    data = {'email': email, 'password': password}
    response = requests.post('http://localhost:5000/users', data=data)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'user created'}


def log_in_wrong_password(email: str, password: str) -> None:
    """Test for login with wrong password"""
    data = {'email': email, 'password': password}
    response = requests.post('http://localhost:5000/sessions', data=data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Test for regsitered user login"""
    data = {'email': email, 'password': password}
    response = requests.post('http://localhost:5000/sessions', data=data)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'logged in'}
    session_id = response.cookies.get('session_id')
    assert session_id is not None
    return session_id


def profile_unlogged() -> None:
    """Test for unlogged profile"""
    response = requests.get('http://localhost:5000/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Test for logged profile"""
    response = requests.get('http://localhost:5000/profile',
                            cookies={'session_id': session_id})
    assert response.status_code == 200
    assert response.json() == {'email': EMAIL}


def log_out(session_id: str) -> None:
    """Test for logout"""
    response = requests.delete('http://localhost:5000/sessions',
                               cookies={'session_id': session_id})
    assert response.status_code == 200
    assert response.json() == {'message': 'Bienvenue'}


def reset_password_token(email: str) -> str:
    """Test for get_reset_password_token"""
    data = {'email': email}
    response = requests.post('http://localhost:5000/reset_password', data=data)
    assert response.status_code == 200
    reset_token = response.json().get('reset_token')
    assert reset_token is not None
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test for update_password"""
    data = {'email': email, 'reset_token': reset_token,
            'new_password': new_password}
    response = requests.put('http://localhost:5000/reset_password', data=data)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'Password updated'}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
