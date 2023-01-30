import pytest

@pytest.fixture()
def person_data_create_payload():
    return {
        "name": "uahduasgd",
        "document_number": "567356"
    }

@pytest.fixture()
def person_data_created_response():
    return {
        "result": "Person sucessfully created."
    }


@pytest.fixture()
def vehicle_data_create_payload():
    return {
        "license_plate": "OUY-7095",
        "color": "yellow",
        "model": "sedan",
        "owner_id": 2
    }


@pytest.fixture()
def vehicle_data_created_response():
    return {
        "result": "Veihicle sucessfully assigned to owner"
    }

@pytest.fixture()
def vehicle_data_error_assign_response():
    return {
        "message": "It is only possible to assign up to 3 vehicles per person"
    }
