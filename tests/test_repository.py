import pytest

from app.domain.entity import User, Product
from app.infrastructure.database.orm import db, UserModel, ProductModel
from app.infrastructure.database.repository.product import ProductRepository
from app.infrastructure.database.repository.user import UserRepository


@pytest.fixture
def init_database():
    db.init(database=":memory:")
    db.connect()
    UserModel.create_table()
    ProductModel.create_table()


def test_create_user_repository(init_database):
    name = "grab"
    _user = User(name=name)
    repository = UserRepository()

    created_user = repository.create(_user)
    # user = repository.find_one(_user)

    assert created_user == _user


def test_find_product_repository(init_database):
    repository = ProductRepository()
    product_id, product_name, product_price = 1, "맥북", 1250000
    _product = Product(id=product_id)

    # Product 생성
    ProductModel.create(name=product_name, price=product_price)

    # Product 조회
    product = repository.find_one(model=_product)

    assert product
