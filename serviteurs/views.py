# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Serviteurs
#from .form import Upadatallinfos
#from django.shortcuts import get_object_or_404


# tout les serviteurs
class Allserviteurs(ListView):
    model = Serviteurs
    context_object_name = "liste_de_serviteurs"
    template_name = "serviteurs/serviteurs_liste.html"


class Detailserviteur(DetailView):
    model = Serviteurs
    template_name = "serviteurs/serviteur_detail.html"

# pour la creation d'un nouveau serviteurs
class CreeServiteur(CreateView):
    template_name = "serviteurs/serviteur_creation.html"
    model = Serviteurs
    fields = '__all__'

class ModifierServiteur(UpdateView):
    template_name = "serviteurs/serviteur_modif.html"
    model = Serviteurs
    fields = "__all__"

