from django.urls import path
from .views import (accesstoken,)


urlpatterns=[
    path('',accesstoken),
]