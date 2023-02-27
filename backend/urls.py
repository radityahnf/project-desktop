from django.urls import path
from backend.views import *

app_name = 'backend'

urlpatterns = [
    path('', show_json, name='show_json'),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('add/', add, name="add"),
    path('favorite/', favorite, name="favorite"),
    path('update/', update, name="update")
    
]