from dataclasses import dataclass
from typing import Optional


@dataclass
class Domain:
    ...


@dataclass
class User(Domain):
    name: str


@dataclass
class Product(Domain):
    id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[int] = None
