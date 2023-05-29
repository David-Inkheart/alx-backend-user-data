# This project covers some concepts on the authentication process and implementation of a Basic Authentication on a simple REST API:
- What authentication means
- What Base64 is
- How to encode/decode Base64
- What Basic Authentication means
- How to send the Authorization header
- Error catching and handling


### [0. Simple-basic-API](./api/v1/app.py)
Download and start your project from this [archive.zip](https://intranet.alxswe.com/rltoken/2o4gAozNufil_KjoxKI5bA)

In this archive, you will find a simple API with one model: `User`. Storage of these users is done via a serialization/deserialization in files.

### **Setup and start server**
```
bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
...
bob@dylan:~$
```

### [1. Error handler: Unauthorized](./api/v1/app.py)
What the HTTP status code for a request unauthorized? `401` of course!

Edit `api/v1/app.py` :
    - Add a new error handler for this status code, the response must be:
    - a JSON: `{"error": "Unauthorized"}`
    - a status code: `401`
    - you must use `jsonify` from `flask`
For testing this new error handler, add a new endpoint in `api/v1/app.py`:
    - Route: `/api/v1/unauthorized`
    - Method: `GET`
    - Use the function `abort` from `flask` to raise the error `401`
By calling `abort(401)`, the error handler for 401 will be executed.

`abort` - [Custom Error Pages](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/) 

### [2. Error handler: Forbidden](./api/v1/auth/auth.py)






# API Usage

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)