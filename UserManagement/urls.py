from django.contrib import admin
from django.urls import path, include
from UserManagement import views

# users/

urlpatterns = [
    path("login/", views.login_user),
    path("logout/", views.logout_user),
    path('copy/', views.mysqlToPG),
]
