# Django Person API Documentation

This repository contains a Django REST API for managing persons. The API allows you to perform CRUD operations (Create, Read, Update, Delete) on person records.

## Table of Contents

- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run the Development Server](#run-the-development-server)
- [Contributing](#contributing)
- [License](#license)

## API Endpoints
- Create a Person:
  - Endpoint: /api/
  - Method: POST

- JSON Request Body Example:
    `{
        "name": "Elon Musk",
    }`

- Retrieve, Update, or Delete a Person by ID:

  - Endpoint: /api/{id}/
  - Methods: GET, PUT, DELETE
  - Example:
    - To retrieve: /api/{id}/ (GET request)
    - To update: /api/{id}/ (PUT request with updated JSON data)
    - To delete: /api/{id}/ (DELETE request)

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



## Prerequisites

Before setting up and running the API on your local system, ensure you have the following prerequisites installed:

- Python (version 3.x) https://www.python.org/downloads/


## Installation

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

## Run the Development Server

Start the Django development server to run the API locally:

  `python3 manage.py runserver`

    The API will be accessible at http://localhost:8000/api/





## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

    Fork the repository on GitHub.
    Clone your fork locally.
    Create a new branch for your feature or bug fix.
    Make your changes and commit them.
    Push your changes to your fork on GitHub.
    Open a pull request to the main repository.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/developerayyo/eportal/blob/main/LICENSE) file for details.