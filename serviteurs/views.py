# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Serviteurs

# tout les serviteurs
class Allserviteurs(ListView):
    model = Serviteurs
    context_object_name = "liste_de_serviteurs"
    template_name = "serviteurs/serviteurs_liste.html"

class Detailserviteur(DetailView):
    model = Serviteurs
    template_name = "serviteurs/serviteur_detail.html"