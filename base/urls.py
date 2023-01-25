from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.landingpage, name="landingpage"),
    path('homepage/', views.homepage, name="homepage"),
    #path('room/<str:pk>/', views.room, name="room"),
]