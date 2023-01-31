from src.repository.database_operations import DatabaseRepository
from src.repository.entities.owner import Owner


class PersonUseCases():
    def __init__(self) -> None:
        self.repository = DatabaseRepository(Owner)

    def create_person(self, data):
        return self.repository.create(data)
    
    def get_owners(self):
        persons = self.repository.get_all()
        return self.format_payload(persons)
    
    @staticmethod
    def format_payload(persons):
        owners = []
        for person in persons:
            vehicles = []
            payload = {
                "id": person.id,
                "name": person.name,
                "document_number": person.document_number,
            }        
            if person.vehicle:
                for vehicle in person.vehicle:
                    vehicles.append({
                        "license_plate": vehicle.license_plate,
                        "color": vehicle.color,
                        "model": vehicle.model
                    })
            else:
                payload.update({"sale_oportunity": person.sale_oportunity})
            
            payload.update({"vehicles": vehicles})
            owners.append(payload)
        
        return owners
