import requests
import json

# Define the base URL of your Django API
BASE_URL = 'https://peterbabalola.info/api/'

# Define headers for JSON content
headers = {'Content-Type': 'application/json'}

# Function to perform a POST request to create a new person
def create_person(name):
    data = {'name': name}
    response = requests.post(BASE_URL, data=json.dumps(data), headers=headers)
    return response

# Function to perform a GET request to retrieve a person by ID
def retrieve_person(person_id):
    response = requests.get(BASE_URL + f'{person_id}/')
    return response

# Function to perform a PUT request to update a person's name by ID
def update_person(person_id, new_name):
    data = {'name': new_name}
    response = requests.put(BASE_URL + f'{person_id}/', data=json.dumps(data), headers=headers)
    return response

# Function to perform a DELETE request to delete a person by ID
def delete_person(person_id):
    response = requests.delete(BASE_URL + f'{person_id}/')
    return response

# Testing CRUD operations
if __name__ == '__main__':
    # Create a new person
    create_response = create_person('Elon Musk')
    if create_response.status_code == 201:
        print('Person created successfully.')
    else:
        print('Failed to create person.')

    # Retrieve the created person by ID
    person_id = create_response.json().get('id')
    retrieve_response = retrieve_person(person_id)
    if retrieve_response.status_code == 200:
        print('Person retrieved successfully:')
        print(retrieve_response.json())
    else:
        print('Failed to retrieve person.')

    # Update the person's name
    update_response = update_person(person_id, 'Updated Name')
    if update_response.status_code == 200:
        print('Person name updated successfully.')
    else:
        print('Failed to update person name.')

    # Delete the person by ID
    delete_response = delete_person(person_id)
    if delete_response.status_code == 204:
        print('Person deleted successfully.')
    else:
        print('Failed to delete person.')
