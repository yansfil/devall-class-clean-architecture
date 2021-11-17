from app.application.interfaces.repository import AbstractRepository
from app.domain.entity import Product


class ProductService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def get_product(self, product_id: int):
        _product = Product(id=product_id)
        product = self.repository.find_one(model=_product)

        return product
