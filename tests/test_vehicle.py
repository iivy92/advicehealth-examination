import json
import requests
import requests_mock
from src.utils.exceptions import InvalidUsage


def test_vehicle_assigned_sucess(vehicle_data_create_payload, vehicle_data_created_response):
    with requests_mock.Mocker() as mock:
        mock.register_uri(
            'POST', 
            'http://localhost:8080/v1/vehicle/assign', 
            json=vehicle_data_created_response
        )
        response = requests.post('http://localhost:8080/v1/vehicle/assign', json=vehicle_data_create_payload)
    
    assert response.status_code == 200
    assert response.text == json.dumps(vehicle_data_created_response)


def test_vehicle_created_error(vehicle_data_create_payload, vehicle_data_error_assign_response):
    with requests_mock.Mocker() as mock:
        mock.register_uri(
            'POST', 
            'http://localhost:8080/v1/vehicle/assign', 
            status_code=400,
            json=vehicle_data_error_assign_response
        )
        response = requests.post('http://localhost:8080/v1/vehicle/assign', json=vehicle_data_create_payload)
    
    assert response.status_code == 400
    assert response.text == json.dumps(vehicle_data_error_assign_response)

