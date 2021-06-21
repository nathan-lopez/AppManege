# from django.shortcuts import render
from django.views.generic import ListView
from .models import Serviteurs

# tout les serviteurs
class Allserviteurs(ListView):
    model = Serviteurs
    context_object_name = "liste_de_serviteurs"
    template_name = "serviteurs/base.html"