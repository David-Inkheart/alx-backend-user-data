# This project covers some concepts on the authentication process and implementation of a Basic Authentication on a simple API:
- What authentication means
- What Base64 is
- How to encode/decode Base64
- What Basic Authentication means
- How to send the Authorization header


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
