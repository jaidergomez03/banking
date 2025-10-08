# authentication_app/urls.py

from django.urls import path
from . import views

# Define el 'namespace' para usarlo en los 'redirects'
app_name = "authentication_app"

urlpatterns=[
    path("", views.index, name="index"),  
    path("countries/", views.country_list, name="country_list"),
    path("countries/<int:pk>/edit/", views.country_edit, name="country_edit"),
]