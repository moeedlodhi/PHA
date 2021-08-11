from django.urls import path
from societies import views

# societies/
urlpatterns = [
    path("create_allotment/", views.create_allotment),
]
