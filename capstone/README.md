# Casting Agency

## Introduction
Casting Agency app.

## Getting Started
### Base URL
You can run the app locally or in Heroku:
- Locally: http://127.0.0.1:5000/
- Heroku: https://capstone-api-heroku.herokuapp.com/ 

### Installing Dependencies
Python Version Used: Python 3.8

Install python dependencies using pip3.
```pip3 install -r requirements.txt```

*All needed variables are saved in setup.sh*

### Run the server locally:

Create a local database using postgresql, run the following:
```
createdb capstone_test
```

Then run the app using this command:
```python3 app.py```

### Authentication: 
Auth0 tokens ae used for the authentication. There are three roles for the casting agency:

**Casting Assistant**

- Can view actors and movies

**Casting Director**

- Can view actors and movies

- Add or delete an actor from the database

- Modify actors or movies

**Executive Producer**

- Can view actors and movies

- Add or delete an actor from the database

- Modify actors or movies

- Add or delete a movie from the database

### Get Authentication token for different roles.
I have created some dummy accounts and assigned them with specific roles. You can login using these credentials to get the access token. After login, look for access token in the browser url.
- Login URL: https://dev-q5n2ze8g.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=oGSoz45p9WV6eaxrKtFMMVSVXO7n6tT4&redirect_uri=http://localhost:5000/login-results

**Casting Assistant**
- Username: minuchinu@gmail.com
- Password: rP;yy5@e

**Casting Director**
- Username: dibyaranjan.sathua@gmail.com
- Password: y~tR.a9N

**Executive Producer**
- Username: renadalmadhix@gmail.com
- Password: :=4=pXYq

## Test
You can test the app by running the test_app.py. We don't need a db dump as data are created on fly during the unittests.
```python3 test_app.py```

Some of the unitests use tokens. Please re-generate tokens for all the roles and add it to setup.sh file. Run setup.sh before running python tests.
```source setup.sh```

## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Resource Not Found"
}
```

### Error Types and Messages
The Casting Agency app will return the below error types when requests fail:
- 404: Resource Not Found
- 422: Not Processable
- 405: Method Not Allowed
- 400: Bad Request
- 500: Internal Server Error

## Resource Endpoint Library
### GET '/movies'
* Genreal
    * Fetches a dictionary of movies
    * Request Arguments: None
    * Returns: An object that contains movies array, and a success boolean value.
* Sample: `curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/movies`

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Fri, 08 Jan 2021 20:58:29 GMT",
            "title": "Dhoom"
        },
        {
            "id": 2,
            "release_date": "Mon, 08 Feb 2021 20:58:29 GMT",
            "title": "Wonderland"
        },
        {
            "id": 3,
            "release_date": "Mon, 08 Mar 2021 20:58:29 GMT",
            "title": "Spiderman"
        },
        {
            "id": 4,
            "release_date": "Thu, 08 Apr 2021 20:58:29 GMT",
            "title": "Wonderwoman"
        }
    ],
    "success": true
}
```


### GET '/actors'
* Genreal
    * Fetches a dictionary of actors
    * Request Arguments: None
    * Returns: An object that contains actors array, and a success boolean value.
* Sample: `curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/actors`

```
{
    "actors": [
        {
            "age": 58,
            "gender": "male",
            "id": 1,
            "name": "Tom Cruise"
        },
        {
            "age": 26,
            "gender": "male",
            "id": 2,
            "name": "Rahul"
        },
        {
            "age": 26,
            "gender": "female",
            "id": 3,
            "name": "Gal Gadot"
        },
        {
            "age": 32,
            "gender": "female",
            "id": 4,
            "name": "Angelina Joile"
        },
        {
            "age": 30,
            "gender": "female",
            "id": 5,
            "name": "Emma"
        }
    ],
    "success": true
}
```

### POST '/movies'
* General
    * Creates a new movie
    * Request Arguments: None
    * Returns: An object that contains a success boolean value and the created movie.
* Sample: `curl http://127.0.0.1:5000/movies -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"title\":\"Wonderwoman\",\"release_date\":\"2021-04-08\"}"`
```
{
    "created": 4,
    "success": true
}
```

### POST '/actors'
* General
    * Creates a new actor
    * Request Arguments: None
    * Returns: An object that contains a success boolean value and the created actor.
* Sample: `curl http://127.0.0.1:5000/actors -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"name\":\"Emma\",\"age\":\"30\",\"gender\":\"female\"}"`
```
{
    "created": 5,
    "success": true
}
```


### PATCH '/movies/1'
* General
    * Updates the specified movie
    * Request Arguments: None
    * Returns: An object that contains a success boolean value and the updated movie.
* Sample: `curl http://127.0.0.1:5000/movies/1 -X PATCH -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"release_date\":\"2021-01-10\"}"`
```
{
    "movie": {
        "id": 2,
        "release_date": "Sun, 10 Jan 2021 00:00:00 GMT",
        "title": "Wonderland"
    },
    "success": true
}
```

### PATCH '/actors/1'
* General
    * Updates the specified actor
    * Request Arguments: None
    * Returns: An object that contains a success boolean value and the updated actor.
* Sample: `curl http://127.0.0.1:5000/actors/1 -X PATCH -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"name\":\"Name changed\"}"`
```
{
    "actor": {
        "age": 14,
        "gender": "male",
        "id": 1,
        "name": "Name changed"
    },
    "success": true
}
```

### DELETE '/movies/2'
* Genreal
    * Removes the specified movie
    * Request Arguments: The movie's ID
    * Returns: An object than contains a success boolean value and the ID of the deleted movie.
* Sample: `curl -X DELETE -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/movies/1`
```
{
    "delete": 1,
    "success": true
}
```

### DELETE '/actors/2'
* Genreal
    * Removes the specified actor
    * Request Arguments: The actor's ID
    * Returns: An object than contains a success boolean value and the ID of the deleted actor.
* Sample: `curl -X DELETE -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/actors/2`
```
{
  "deleted": 2,
  "success": true
}
```
