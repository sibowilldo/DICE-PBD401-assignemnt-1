# Teachers Assistant & Tutors Opportunities Portal by D.I.C.E Systems

## Getting Started

### Installing Dependencies

#### Python 3.11

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


## Setup and Activate Virtual Environment
#### Virtual Environment

It's recommended that you work within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

From within the `/backend` directory first ensure you are working using your created virtual environment, by running

```bash
python3 -m venv venv && source venv/bin/activate
```

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

Rename `.env.example` to `.env`
```bash
cp .env.example .env
```
The necessary configuration for running the Flask App should already be set, `FLASK_APP=src/app.py` and `FLASK_DEBUG=True`

To run the server, execute:

```bash
flask run
```
