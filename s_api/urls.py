from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignUpUser),
    path('users/',views.GetAllUser),
    path('users/<int:pk>/',views.GetOwnCodeDatas),
    path('login/<int:pk>/',views.LoginUser),
    path('add/',views.AddNewCode)
]