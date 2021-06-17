from django.urls import path
from . import views
urlpatterns = [
    path('',views.input,name='input'),
    path('users/',views.users,name='user'),
]
