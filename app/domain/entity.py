class Entity:
    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.id == o.id
        return False
