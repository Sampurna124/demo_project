from django.urls import path
from .views import FirstApi

urlpatterns=[
    path('first/',FirstApi.as_view()),
]