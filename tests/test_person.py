import json
import requests
import requests_mock
from src.utils.exceptions import InvalidUsage


def test_person_created_sucess(person_data_create_payload, person_data_created_response):
    with requests_mock.Mocker() as mock:
        mock.register_uri(
            'POST', 
            'http://localhost:8080/v1/person/create', 
            json=person_data_created_response
        )
        response = requests.post('http://localhost:8080/v1/person/create', json=person_data_create_payload)
    
    assert response.status_code == 200
    assert response.text == json.dumps(person_data_created_response)


def test_person_created_error(person_data_create_payload, person_data_created_response):
    with requests_mock.Mocker() as mock:
        mock.register_uri(
            'POST', 
            'http://localhost:8080/v1/person/create', 
            status_code=400
        )
        response = requests.post('http://localhost:8080/v1/person/create', json=person_data_create_payload)
    
    assert response.status_code == 400
