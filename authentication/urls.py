from django.urls import path
from . import views
app_name = 'banking'
urlpatterns = [
 path('countries/', views.country_list, name='country_list'),
 path('countries/<int:pk>/edit/', views.country_edit, name='country_edit'),
]
