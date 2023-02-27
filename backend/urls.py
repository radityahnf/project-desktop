from django.urls import path
from backend.views import *

app_name = 'backend'

urlpatterns = [
    path('', show_json, name='show_json'),
    path('login/', login, name="login")
]