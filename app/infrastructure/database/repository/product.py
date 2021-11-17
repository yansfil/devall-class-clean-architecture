from app.application.interfaces.repository import AbstractRepository
from app.domain.entity import Product
from app.infrastructure.database.orm import ProductModel


class ProductRepository(AbstractRepository):
    def create(self, model: Product):
        ...

    def find_one(self, model: Product):
        product_id = model.id

        product = ProductModel.select().where(ProductModel.id == product_id).first()
        if not product:
            return None
        return Product(id=product.id, name=product.name, price=product.price)
