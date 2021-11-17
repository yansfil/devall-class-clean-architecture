from typing import Optional

import uvicorn
from fastapi import FastAPI
from app.controller.user import signup
from app.infrastructure.database.orm import db, UserModel


def create_app():
    app = FastAPI()
    app.add_api_route(path="/user", methods=["POST"], endpoint=signup)

    return app


def init_db():
    db.connect()
    UserModel.create_table()


app = create_app()

if __name__ == "__main__":
    init_db()

    uvicorn.run(
        "app.infrastructure.fastapi.main:app", host="0.0.0.0", port=8000, reload=True
    )
