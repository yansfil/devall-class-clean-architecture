from app.domain.entity import User


def create_user(user_name: str):
    user = User(name=user_name)
    return user
