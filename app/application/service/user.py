from app.application.interfaces.repository import AbstractRepository
from app.domain.entity import User


class UserService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def create_user(self, user_name: str):
        # 데이터베이스에 저장
        _user = User(name=user_name)
        # 데이터베이스에서 해당 이름이 있는지 확인하고, 있다면 Exception을 발생
        if self.repository.find_one(model=_user):
            raise ValueError("유저가 이미 존재합니다.")
        user = self.repository.create(_user)

        return user
