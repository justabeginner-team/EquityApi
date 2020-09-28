## EquityApi (Jenga-Api) 
  

![Labeler](https://github.com/justabeginner-team/EquityApi/workflows/Labeler/badge.svg)

Generating key pairs
  run this command on the terminal.
```bash
$ python manage.py keypair -gk GEN_KEY  
```
or
```bash
$ python manage.py keypair --genkey GEN_KEY 
```
 ### Note better 
  pass argument to the signature function and obtain a tuple 
  
 ```python
def signature(requestfields):
    pass
``` 
 ### TO NOTE
- introduced celery to run eazzypaypush task
<br />
**run this command on a seperate terminal**
```bash
$ celery -A equityapi worker -l info -Q eazzypaypush_request,celery
```




