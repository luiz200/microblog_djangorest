# DjangoRESTFramework - API Documentation

This is the API documentation for the DjangoRESTFramework application, which allows data insertion using Insomnia.

## Environment Setup

Before getting started with the application, make sure you have the following:

- Python 3.6 or higher installed on your system.
- Django 3.0 or higher installed.
- DjangoRESTFramework 3.12 or higher installed.

## Installation

1. Clone the DjangoRESTFramework repository:

```bash
$ git clone https://github.com/luiz200/microblog_djangorest.git
$ cd django-rest-app
```

2. Create and activate a virtual environment (optional but recommended):

```bash
$ python3 -m venv env
$ source venv/bin/activate
```

3. Install project dependencies:

```bash
$ pip install -r requirements.txt
```

4. Run Django migrations:

```bash
$ python manage.py migrate
```

5. Start the development server:

```bash
$ python manage.py runserver
```

#Using Insomnia for Data Insertion

nsomnia is an API testing tool that allows you to send HTTP requests to your server. Follow the steps below to use Insomnia for data insertion in the DjangoRESTFramework application.

1. Download and install Insomnia: https://insomnia.rest/

2. Open Insomnia and click on "Create" to create a new workspace.

3. Select the "POST" method to create a new request.

4. Enter the endpoint URL for data insertion, for example: http://localhost:8000/api/data/.

5. In the "Headers" panel, add the Content-Type header with the value application/json.

6. In the "Body" panel, select the "JSON" option and enter the data you want to insert in JSON format. For example:

```json
{
  "field1": "value1",
  "field2": "value2",
  "field3": "value3"
}
```

7. Click on "Send" to send the request.
8. Check the response received from the server to verify if the data was successfully inserted
