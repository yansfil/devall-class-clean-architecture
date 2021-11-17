import pytest
from starlette.testclient import TestClient

from app.infrastructure.database.orm import db, UserModel, ProductModel
from app.infrastructure.fastapi.main import create_app


@pytest.fixture
def init_database(tmpdir):
    db.init(database=f"{tmpdir}/database.db")
    db.connect()
    UserModel.create_table()
    ProductModel.create_table()
    yield db
    db.drop_tables([UserModel, ProductModel])


@pytest.fixture
def fastapi_client(init_database):
    return TestClient(app=create_app(initialize_db=False))


def test_get_product_api(fastapi_client):
    product_id = 1
    ProductModel.bulk_create([ProductModel(name="키보드", price=30000)])

    with fastapi_client as client:
        result = client.get(f"products/{product_id}").json()

        assert result == {"id": 1, "name": "키보드", "price": 30000}
