from app.application.interfaces.repository import AbstractRepository
from app.domain.entity import User


class FakeUserRepository(AbstractRepository):
    def __init__(self, users=[]):
        self.users = users

    def create(self, model: User):
        self.users.append(model)
        return model

    def find_one(self, model: User):
        for _user in self.users:
            if _user.name == model.name:
                return model
        return None
