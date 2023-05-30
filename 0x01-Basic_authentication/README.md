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
What the HTTP status code for a request where the user is authenticate but not allowed to access to a resource? `403` of course!

Edit `api/v1/app.py` :
    - Add a new error handler for this status code, the response must be:
    - a JSON: `{"error": "Forbidden"}`
    - a status code: `403`
    - you must use `jsonify` from `flask`
For testing this new error handler, add a new endpoint in `api/v1/views/index.py`:
    - Route: `GET /api/v1/forbidden`
    - This endpoint must raise a `403` error by using `abort`
By calling `abort(403)`, the error handler for 403 will be executed.

### [3. Auth class](./api/v1/auth/auth.py)
Now you will create a class to manage the API authentication.
    - Create a folder `api/v1/auth`
    - Create an empty file `api/v1/auth/__init__.py`
    - Create a class `Auth`:
        - in the file `api/v1/auth/auth.py`
        - import `request` from `flask`
        - class name: `Auth`
        - public method: `def require_auth(self, path: str, excluded_paths: List[str]) -> bool`:
        that returns False - `path` and `excluded_paths` will be used later, now, you don’t need to take care of them
        - public method: `def authorization_header(self, request=None) -> str`: that returns `None` - `request` will be the Flask request object
        - public method: `def current_user(self, request=None) -> TypeVar('User')`: that returns `None` - `request` will be the Flask request object
This class is the template for all authentication system you will implement.

### [4. Define which routes don't need authentication](./api/v1/auth/auth.py)
Update the method `def require_auth(self, path: str, excluded_paths: List[str]) -> bool:` in `Auth` that returns `True` if the `path` is not in the list of strings `excluded_paths`:

- Returns `True` if `path` is `None`
- Returns `True` if `excluded_paths` is `None` or `empty`
- Returns `False` if `path` is in e`xcluded_paths`
- You can assume `excluded_paths` contains string `path` always ending by a `/`
- This method must be slash tolerant: `path=/api/v1/status` and `path=/api/v1/status/` must be returned False if `excluded_paths` contains `/api/v1/status/`

### [5. Request validation!](./api/v1/auth/auth.py)
Now you will validate all requests to secure the API:

Update the method def authorization_header(self, request=None) -> str: in api/v1/auth/auth.py:

- If request is None, returns None
- If request doesn’t contain the header key Authorization, returns None
- Otherwise, return the value of the header request Authorization
Update the file api/v1/app.py:

- Create a variable auth initialized to None after the CORS definition
- Based on the environment variable AUTH_TYPE, load and assign the right instance of authentication to auth
  - if auth:
    - import Auth from api.v1.auth.auth
    - create an instance of Auth and assign it to the variable auth
Now the biggest piece is the filtering of each request. For that you will use the Flask method before_request

- Add a method in api/v1/app.py to handler before_request
  - if auth is None, do nothing
  - if request.path is not part of this list ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/'], do nothing - you must use the method require_auth from the auth instance
  - if auth.authorization_header(request) returns None, raise the error 401 - you must use abort
  - if auth.current_user(request) returns None, raise the error 403 - you must use abort

### [6. Basic auth](./api/v1/auth/basic_auth.py)
Create a class `BasicAuth` that inherits from `Auth`. For the moment this class will be empty.

Update `api/v1/app.py` for using `BasicAuth` class instead of `Auth` depending of the value of the environment variable `AUTH_TYPE`, If `A`UTH_TYPE` is equal to `basic_auth`:

- import `BasicAuth `from `api.v1.auth.basic_auth`
- create an instance of `BasicAuth` and assign it to the variable `auth`
Otherwise, keep the previous mechanism with `auth` an instance of `Auth`.

__________________________________
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