from dataclasses import dataclass


@dataclass
class Domain:
    ...


@dataclass
class User(Domain):
    name: str


@dataclass
class Product(Domain):
    id: int
    name: str
    price: int
