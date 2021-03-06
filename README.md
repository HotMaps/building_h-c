HOTMAPS building_h-c API
==========================

This project is dedicated to the Hotmaps building_h-c API.

It's based on the Hotmaps API template that you can find here: [https://github.com/HotMaps/api-template](https://github.com/HotMaps/api-template).


Project Structure
-----------------

### Features

This repository includes the features developed within WP3 of the Hotmaps project: [http://www.hotmaps-project.eu](http://www.hotmaps-project.eu)
A short description of each features can be found here:

* [F13: Short Description](documentation/F_13.md)
* [F14: Short Description](documentation/F_14.md)
* [F23: Short Description](documentation/F_23.md)
* [F63: Short Description](documentation/F_63.md)
* [F107: Short Description](documentation/F_107.md)

### Root folder

Folders:

* `app` - Our application is here.
* `tests` - The unit test you will do on your project.
* `documentation` - A short documentation of each feature.

Files:

* `README.md`
* `Dockerfile` - Docker config file which is used to build a Docker image
  running this RESTful API Server example.
* `.gitignore` - Lists files and file masks of the files which should not be
  added to git repository.
* `Author` - A list of the person who have worked on the project and how to contact them
* `LICENSE` - The used license
* `docker_restart.sh` - File to run the docker container

### Application Structure

```
app/
├── __init__.py
├── settings.py
├── extensions
│    ├── __init__.py
│    └── api
│        ├── __init__.py
│        ├── api.py
│        └── parameters.py
├── flask_restplus_patched
│    └── ...
└── modules
    ├── __init__.py
    ├── api
    │   └── __init__.py
    ├── common
    │   ├── __init__.py
    │   ├── customFields.py
    │   ├── schemas.py
    │   ├── CM
    │   │   └── Calculation modules for features
    │   ├── AD
    │   │   └── dummy data for features
    │   └── FEAT
    │   │   └── F13_district_heating_potential
    │   │   └── F14_individual_heat_supply_costs_per_building
    │   │   └── F23_district heating grid investment model
    │   │   └── F63_bottomup_heat_density_map
    │   │   └── F107_scaling_hdm
    ├── F13
    │   ├── __init__.py
    │   ├── models.py
    │   ├── parameters.py
    │   ├── resources.py
    │   └── schemas.py
    ├── F14
    │   ├── __init__.py
    │   ├── models.py
    │   ├── parameters.py
    │   ├── resources.py
    │   └── schemas.py
    ├── F23
    │   ├── __init__.py
    │   ├── models.py
    │   ├── parameters.py
    │   ├── resources.py
    │   └── schemas.py
    ├── F63
    │   ├── __init__.py
    │   ├── models.py
    │   ├── parameters.py
    │   ├── resources.py
    │   └── schemas.py
    ├── F107
    │   ├── __init__.py
    │   ├── models.py
    │   ├── parameters.py
    │   ├── resources.py
    │   └── schemas.py
    └── example
        ├── __init__.py
        ├── models.py
        ├── parameters.py
        ├── resources.py
        └── schemas.py

```

* `app/requirements.txt` - The list of Python (PyPi) requirements.
* `app/__init__.py` - The entrypoint to this RESTful API Server example
  application (Flask application is created here).
* `app/extensions` - All extensions (e.g. SQLAlchemy, OAuth2) are initialized
  here and can be used in the application by importing as, for example,
  `from app.extensions import db`.
* `app/modules` - All endpoints are expected to be implemented here in logicaly
  separated modules. It is up to you how to draw the line to separate concerns
  (e.g. you can implement a monolith `blog` module, or split it into
  `topics`+`comments` modules).
* `app/modules/common` - This regroup the features that can be used by any of those modules in order to avoid complexifying imports, it regroups schemas and final string name.  
* `app/flask_restplus_patched` - This is the patched version of flask restplus that has been made by frol, it allows flask restplus to handle marshmallow better.
### Module Structure

Once you added a module name into `config.ENABLED_MODULES`, it is required to
have `example.init_app(app, **kwargs)` function. Everything else is
completely optional. Thus, here is the required minimum:

```
example
    ├── __init__.py
    ├── models.py
    ├── parameters.py
    ├── resources.py
    └── schemas.py
```

 where `__init__.py` will look like this:

```python
from extensions.api import api
from . import resources

def init_app(app, **kwargs):
    api.add_namespace(resources.api)
```

This example will add the namespace of the resources to the api list. You will learn more about the code functionment in the next section.

`models.py` contains the different models from the db that you will use in this project (you can remove if you don't need it)

`parameters.py` contains the parameters you will use for your different api request

`resources.py` contains the diffrent function that will be used by your api

`schemas.py` contains the different schemas (using marshmallow) that you will need in your API

### Tests structure
```
tests/
└── modules
    ├── __init__.py
    └── example
        ├── __init__.py
        └── resources
            ├── __init__.py
            ├── payload.txt
            └── test_example_area.py
```
* `tests/modules` - All tests on all modules, here, you can tests some features (schemas, models, ...) on the main folder.

###Tests module Structure
```
example
   ├── __init__.py
   └── resources
       ├── __init__.py
       ├── payload.txt
       └── test_example_area.py
```

`resources` - Put all the operation related to the module API inside.

`resources/payload.txt` contains the response that is awaited by the query, if the response differs from the payload, the test will fail.

`resources/test_example_area.py` contains the concrete test that will be executed.

How to run the service ?
--------------------------------

Once you have configured your docker container in an appropriate way, you simply have to launch your app using those commands on the root repository of the project (where the Dockerfile is located)

```
(sudo) docker build -t hotmaps/building-hc .
(sudo) docker run --name building-hc -p 9006:80 -d hotmaps/building-hc
```

You can also use `docker_restart.sh` instead.

The hostport is the port that will be used to access the service on the host machine. 
    Example: -p 8080:80 will run the service on the port 80 of the docker container and be accessible on the port 8080 of the host machine(localhost:8080/api/v1).

On Windows 7: Use your docker machine ip (`docker-machine ip`)	

This will launch the server using gunicorn and the wsgi file

The command creates an application by running
[`app/wsgi.py:application = create_app()`](app/wsgi.py) function, which in its turn:

1. loads an application config;
2. initializes extensions:
3. initializes modules:

Modules initialization calls `init_app()` in every enabled module
(listed in `config.ENABLED_MODULES`).

[`app/modules/example/__init__.py:init_app()`](app/modules/example/__init__.py)
imports and registers `api` instance of (patched) `flask_restplus.Namespace`
from `.resources`. Flask-RESTPlus `Namespace` is designed to provide similar
functionality as Flask `Blueprint`.

[`api.route()`](app/modules/example/resources.py) is used to bind a
resource (classes inherited from `flask_restplus.Resource`) to a specific
route.

Lastly, every `Resource` should have methods which are lowercased HTTP method
names (i.e. `.get()`, `.post()`, etc). This is where users' requests end up.


How to run tests ?
--------------------------------
cd tests

copy `test_settings_example.py` to `test_settings.py`

adapt `test_settings.py` (change localhost to ip)

run pytest

Dependencies
------------

### Project Dependencies

* [**Python**](https://www.python.org/) 3.5+ / pypy2 (2.5.0)
* [**flask-restplus**](https://github.com/noirbizarre/flask-restplus) (+
  [*flask*](http://flask.pocoo.org/))
* [**sqlalchemy**](http://www.sqlalchemy.org/) (+
  [*flask-sqlalchemy*](http://flask-sqlalchemy.pocoo.org/)) - Database ORM.
* [**sqlalchemy-utils**](https://sqlalchemy-utils.rtdf.org/) - for nice
  custom fields (e.g., `PasswordField`).
* [**alembic**](https://alembic.rtdf.org/) - for DB migrations.
* [**marshmallow**](http://marshmallow.rtfd.org/) (+
  [*marshmallow-sqlalchemy*](http://marshmallow-sqlalchemy.rtfd.org/),
  [*flask-marshmallow*](http://flask-marshmallow.rtfd.org/)) - for
  schema definitions. (*supported by the patched Flask-RESTplus*)
* [**webargs**](http://webargs.rtfd.org/) - for parameters (input arguments).
  (*supported by the patched Flask-RESTplus*)
* [**apispec**](http://apispec.rtfd.org/) - for *marshmallow* and *webargs*
  introspection. (*integrated into the patched Flask-RESTplus*)
* [**Swagger-UI**](https://github.com/swagger-api/swagger-ui) - for interactive
  RESTful API documentation.

### Patched Dependencies

* **flask-restplus** is patched to handle marshmallow schemas and webargs
  input parameters
  ([GH #9](https://github.com/noirbizarre/flask-restplus/issues/9)).
* **swagger-ui** (*the bundle is automatically downloaded on the first run*)
  just includes a pull-request to support Resource Owner Password Credentials
  Grant OAuth2 (aka Password Flow)
  ([PR #1853](https://github.com/swagger-api/swagger-ui/pull/1853)).


Installation
------------
### From sources

#### Clone the Project

```bash
$ git clone https://github.com/HotMaps/api-template
```

#### Setup Environment

You will need an installation of docker to run this
you will need to connect port 80 of the container with port 9006 of the host using TCP and choose the dockerfile as deployment source

#### Run Server

NOTE: All dependencies and database migrations will be automatically handled,
so go ahead and turn the server ON! (Read more details on this in Tips section)

simply launch the project with docker configured
