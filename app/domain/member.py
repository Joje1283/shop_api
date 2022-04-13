from .address import Address


class Member:
    id: str
    name: str
    address: Address

    def __init__(self, id: str, name: str, address: Address):
        self.id: str = id
        self.name: str = name
        self.address: Address = address

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Member):
            return self.id == o.id

        return False
