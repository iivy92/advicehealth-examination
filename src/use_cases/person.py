from src.repository.database_operations import DatabaseRepository
from src.repository.entities.owner import Owner


class PersonUseCases():
    def __init__(self) -> None:
        self.repository = DatabaseRepository(Owner)

    def create_person(self, data):
        return self.repository.create(data)


