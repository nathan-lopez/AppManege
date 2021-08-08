from django.urls import path
from .views import Serviteurs_par_departement
# les route d'urls pour l'application departement

urlpatterns = [
    path('', Serviteurs_par_departement.as_view(), name='liste_departement')
]