from django.urls import path
from .views import Liste_de_departement
# les route d'urls pour l'application departement

urlpatterns = [
    path('', Liste_de_departement, name='liste_departement')
]