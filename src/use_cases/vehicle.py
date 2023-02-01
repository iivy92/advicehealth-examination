from src.repository.database_operations import DatabaseRepository
from src.repository.entities.vehicle import Vehicle


class VeihicleUseCases():
    def __init__(self) -> None:
        self.repository = DatabaseRepository(Vehicle)

    def assign_veihicle(self, data):
        vehicles = self.repository.get_vehicles_by_owner_id(data["owner_id"])
        self.check_vehicle_quantity(vehicles)
        return self.repository.create(data)
    
    @staticmethod
    def check_vehicle_quantity(vehicles):
        if len(vehicles) >= 3:
            raise Exception('It is only possible to assign up to 3 vehicles per person')
