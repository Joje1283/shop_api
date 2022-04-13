from dataclasses import dataclass


@dataclass
class Address:
    city: str
    street: str
    zipcode: str
