from django.views.generic import TemplateView, CreateView, ListView #DetailView
from .models import Agape, Culte, CulteSpecial, Enseignement, Priere, Partage
# Create your views here.

class Index(TemplateView):
    template_name = "evenements/index.html"

class NewEvent(TemplateView):
    template_name = "evenements/creer_evenement.html"

class CreatAgape(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model =Agape


class CreatCulte(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model =Culte

class CreatPartage(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model = Partage

class CreatCulteSpecial(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model =CulteSpecial


class CreatEnseignement(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model =Enseignement


class CreatPriere(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model =Priere

# vu de listing



class ListAgape(ListView):
    template_name = "evenements/index.html"
    fields = "__all__"
    model =Agape
    context_object_name = "list_agape"


class ListCulte(ListView):
    template_name = "evenements/index.html"
    fields = "__all__"
    model =Culte
    context_object_name = "list_culte"


class ListPartage(ListView):
    template_name = "evenements/index.html"
    fields = "__all__"
    model = Partage
    context_object_name = "list_partage"


class ListCulteSpecial(ListView):
    template_name = "evenements/index.html"
    fields = "__all__"
    model =CulteSpecial
    context_object_name = "list_cultespecial"



class ListEnseignement(ListView):
    template_name = "evenements/index.html"
    fields = "__all__"
    model =Enseignement
    context_object_name = "list_enseignement"



class ListPriere(ListView):
    template_name = "evenements/index.html"
    fields = "__all__"
    model =Priere
    context_object_name = "list_priere"



