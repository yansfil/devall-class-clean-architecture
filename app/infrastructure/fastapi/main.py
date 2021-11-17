from typing import Optional

import uvicorn
from fastapi import FastAPI

from app.controller.product import find_product
from app.controller.user import signup
from app.infrastructure.database.orm import db, UserModel, ProductModel


def create_app(initialize_db=False):
    app = FastAPI()
    app.add_api_route(path="/users", methods=["POST"], endpoint=signup)
    app.add_api_route(
        path="/products/{product_id}", methods=["GET"], endpoint=find_product
    )
    if initialize_db:
        init_db()
    return app


def init_db():
    db.init(database="database.db")
    db.connect()
    UserModel.create_table()
    ProductModel.create_table()


app = create_app(initialize_db=True)

if __name__ == "__main__":
    uvicorn.run(
        "app.infrastructure.fastapi.main:app", host="0.0.0.0", port=8000, reload=True
    )
