# EquityApi (Jenga-Api) ![Labeler](https://github.com/justabeginner-team/EquityApi/workflows/Labeler/badge.svg)

# Documentation
## Getting Started
Before installing the package get your Jenga API credentials by creating an account [here.](https://developer.jengaapi.io)
## Installation
1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/), run `virtualenv venv` and then `source venv/bin/activate`
    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/), run `mkvirtualenv venv`
2. Install equity-jenga-api
```bash
# In terminal do:
pip install equity-jenga-api
```
3. Are you a developer? Run the following commands to build from source:-

```bash
$ git clone 
$ cd equity-jenga-api
```
4. Configure your settings.py as follows:
Get to know how to use python-decouple [here.](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)
 ```python
from decouple import config

INSTALLED_APPS = [
    # ...
    'equity-jenga-api']

'''
Configure the following at the bottom of your settings.py
'''

# generated password in jengahq
PASSWORD = config('PASSWORD')

# generated merchant code from jengahq
MERCHANT_CODE = config('MERCHANT_CODE')

# generated api key from jengahq
API_KEY = config('API_KEY')

# Environment is either sandbox or production
ENVIRONMENT = config('ENVIRONMENT')

# base url for api endpoints
UAT_URL = config('UAT_URL')
PRODUCTION_URL = config('PRODUCTION_URL')

# allows to generate a new token before the it expires minus threshold is over, set this value to 600
TOKEN_THRESHOLD = config('TOKEN_THRESHOLD')


CELERY_BROKER_URL = 'amqp://localhost'
```
## Configuration
1. Generate your set of public and private keys which will be stored in a file .JengaApi in the root of your project:
  run this command on the terminal.
```bash
$ python manage.py keypair -gk GEN_KEY  
```
   or
```bash
$ python manage.py keypair --genkey GEN_KEY 
```
2. To generate a signature pass arguments to the signature function and obtain a tuple 
  
 ```python

from equitycore.jenga import signature

# assuming you have a variable fields set it to be a tuple of arguments to be signed in their appropriate order
fields=()
signed_data=signature(fields)
``` 
3. To generate a token:
```console
# run the following in the terminal
python manage.py shell

# imports AuthToken
from equitycore.models import AuthToken

# gets token
AuthToken.objects.getaccesstoken()
``` 
4. Celery worker to run background tasks.
- We have seen it best to use celery to run payments as background tasks, get up-to speed on celery [here](https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html):-
- Run this command on a separate terminal
```bash
 $ celery -A equityapi worker -l info -Q eazzypaypush_request,celery,lipanampesa_request, merchant_request
```

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# Support

# Licence

