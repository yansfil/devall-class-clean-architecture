from fastapi import HTTPException

from app.application.service.user import UserService
from app.infrastructure.database.repository.user import UserRepository


def signup(user_name):
    user_service = UserService(repository=UserRepository())
    try:
        user = user_service.create_user(user_name=user_name)
        return user
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
