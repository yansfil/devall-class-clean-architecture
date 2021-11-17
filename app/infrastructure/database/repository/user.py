from app.application.interfaces.user_repository import AbstractRepository
from app.domain.entity import User
from app.infrastructure.database.orm import UserModel


class UserRepository(AbstractRepository):
    def create(self, model: User):
        UserModel.create(name=model.name)
        return model

    def find_one(self, model: User):
        user = UserModel.select().where(UserModel.name == model.name).first()

        if not user:
            return None
        return User(name=user.name)
