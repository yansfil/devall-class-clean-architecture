from dataclasses import dataclass


@dataclass
class Domain:
    ...


@dataclass
class User(Domain):
    name: str
