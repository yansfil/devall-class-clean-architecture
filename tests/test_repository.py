import pytest

from app.domain.entity import User
from app.infrastructure.database.orm import db, UserModel
from app.infrastructure.database.repository.user import UserRepository


@pytest.fixture
def init_database():
    db.init(database=":memory:")
    db.connect()
    UserModel.create_table()


def test_create_user_repository(init_database):
    name = "grab"
    _user = User(name=name)
    repository = UserRepository()

    created_user = repository.create(_user)
    # user = repository.find_one(_user)

    assert created_user == _user
