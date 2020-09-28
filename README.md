# EquityApi (Jenga-Api) 
  

![Labeler](https://github.com/justabeginner-team/EquityApi/workflows/Labeler/badge.svg)

# Documentation
# Getting Started

## Installation
1. Install equity-jenga-api
```bash
# In terminal do:
pip install equity-jenga-api
```

2. Are you a developer? Run the following commands to build from source:-

```bash
$ git clone 
$ cd equity-jenga-api
```

3. Configure your settings.py as follows:
 ```python
from decouple import config

INSTALLED_APPS = [
    # ...
    'equity-jenga-api']

# generated merchant code for jengahq
MERCHANT_CODE = config('MERCHANT_CODE')
# generated api key from jengahq
API_KEY = config('API_KEY')
# to determine whether its sandbox or production
ENVIRONMENT = config('ENVIRONMENT')

SANDBOX_URL = config('SANDBOX_URL')
PRODUCTION_URL = config('PRODUCTION_URL')
# allows to generate a new token before the it expires minus threshold is over
TOKEN_THRESHOLD = config('TOKEN_THRESHOLD')
```
## Configuration
1. Generate your set of public and private keys:
  run this command on the terminal.
```bash
python manage.py keypair -gk GEN_KEY  
```
or
```bash
python manage.py keypair --genkey GEN_KEY 
```

2. To generate a signature pass arguments to the signature function and obtain a tuple 
  
 ```python
from equitycore.jenga import signature

# assuming you have a variable fields set it to be a tuple of arguments to be signed in their appropriate order
fields=()
signed_data=signature(fields)
``` 

# Contributing

# Support

# Licence