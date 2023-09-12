# Django API Documentation

Welcome to the documentation for our Django API. This API allows you to manage persons and perform CRUD operations on them. Here, you will find information about the API's endpoints, request/response formats, sample usage, known limitations, and setup instructions.

## API Endpoints

### Create a Person

- **Endpoint**: `/api/`
- **Method**: POST
- **Request Format**:
  ```json
  {"name": "John Doe"}
- **Response Format**:
  ```json
  {
    "id": 1
    "name": "John Doe"
    }

### Retrieve a Person

- **Endpoint**: `/api/{id}/`
- **Method**: GET
- **Response Format**:
  ```json
  {
    "id": 1
    "name": "John Doe"
    }

 ### Update a Person

- **Endpoint**: `/api/{id}/`
- **Method**: PUT
- **Request Format**:
  ```json
  {
    "name": "John R. Doe"
    }   
- **Response Format**:
  ```json
  {
    "name": "John R. Doe"
    }   

 ### Delete a Person

- **Endpoint**: `/api/{id}/`
- **Method**: DELETE
- **Response Format**: Nil

## Usage Examples

Here are some usage examples to interact with the API using CURL:

1. Create a New Person(POST Request):

    To create a new person, you can make a POST request with a JSON body containing the person's details. In this example, we'll create a person named "Elon Musk":

    `curl -X POST -H "Content-Type: application/json" -d '{"name": "Elon Musk"}' https://peterbabalola.info/api/`

    response: `{"id":18,"name":"Elon Musk"}`

2. Retrieve a Person (GET Request):

    To retrieve a person, you can make a GET request to the API endpoint with the person's id as a parameter. In this example, we'll retrieve the person named "Elon Musk":

    `curl https://peterbabalola.info/api/18/`

    response: `{"id":18,"name":"Elon Musk"}`

3. Update a Person's Information (PUT Request):

    To update a person's information, you can make a PUT request with the updated JSON data and the person's id as parameter. In this example, we'll update the name of "Elon Musk" to "Elon R. Musk":

    `curl -X PUT -H "Content-Type: application/json" -d '{"name": "Elon R. Musk"}' https://peterbabalola.info/api/18/`

    response: `{"id":18,"name":"Elon R. Musk"}`

4. Delete a Person (DELETE Request):

    To delete a person, you can make a DELETE request to the API endpoint with the person's id as a parameter. In this example, we'll delete the person named "Elon R. Musk":

    `curl -X DELETE https://peterbabalola.info/api/18/`

    response: Nil,
    To confirm deleted person, perform a GET Request, you should get this response: `{"detail":"Not found."}`

These curl commands demonstrate how to perform CRUD operations based on a person's name and id using this API. You can replace "Elon Musk" with the name of the person you want to create, retrieve, update, or delete.

### Limitations and Assumptions

 - The API assumes that a person's name is a string containing only letters, spaces, and dots. Integers and other characters are not allowed.
 - Error handling is minimal in this documentation. In a production environment, comprehensive error handling and validation should be implemented.

### Setup and Deployment

To set up and deploy the API locally or on a server, follow these steps:

1. Clone this repository to your local machine:

    `git clone https://github.com/developerayyo/HNGTasks.git`
    `cd HNGTasks`

2. Create a virtual environment (recommended) and activate it:

    `python3 -m venv venv`
    `source venv/bin/activate`

3. Install project dependencies:

    `pip install -r requirements.txt`

4. Required Environment Variable

    `touch .env`
      
      add this to .env:

      ```
      DEBUG=True
      SECRET_KEY=your-secret-key-here
      ```


5. Apply database migrations:

    `python3 manage.py makemigrations`
    `python3 manage.py migrate`

6. Run Developement Server:
    `python3 manage.py runserver`
        The API will be accessible at http://localhost:8000/api/

For production deployment, refer to your hosting provider's documentation for guidance on deploying Django applications.