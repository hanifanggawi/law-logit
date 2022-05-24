from django.urls import path
from .views import *

app_name = "jadwal"

urlpatterns = [
    path("", log_queries),
]