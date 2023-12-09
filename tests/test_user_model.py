# pylint: disable=missing-module-docstring, unused-argument, unused-import
# pylint: disable=missing-function-docstring
import pytest
from app.models.portal_user import PortalUserModel
from .data_populator import populate_tables

def test_create_user(db):
    user_id = PortalUserModel().create(
        'test_user',
        'justapass'
    )
    assert user_id == 1

@pytest.mark.parametrize("user_id, expected", [
    (1, True),
    (2, False)
])
def test_user_exists(db, user_id, expected):
    populate_tables(['portal_user'])
    exists = PortalUserModel().user_exists(user_id)
    assert exists is expected

@pytest.mark.parametrize("user_id, expected", [
    (1, 'test_user'),
    (2, None)
])
def test_get_user(db, user_id, expected):
    populate_tables(['portal_user'])
    user = PortalUserModel().get({'id': user_id})
    if user:
        assert user.username == expected
    else:
        assert user is None

# @pytest.mark.parametrize("username,password,expected", [
#     ('test_user','justapass', True),
#     ('foobar', 'blabla', False)
# ])
# def test_authenticate_user(db, username, password, expected):
#     populate_tables(['dashboard_users'])
#     is_auth = UserModel().authenticate_user(username, password)
#     assert is_auth is expected
