from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignUpUser),
    path('users/',views.GetAllUser),
]