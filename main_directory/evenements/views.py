from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Agape, Culte, CulteSpecial, Enseignement, Priere, Partage
# Create your views here.

class Index(TemplateView):
    template_name = "evenements/index.html"


class NewEvent(TemplateView):
    template_name = "evenements/creer_evenement.html"


class CreatAgape(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model = Agape


class CreatCulte(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model = Culte

class CreatPartage(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model = Partage

class CreatCulteSpecial(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model = CulteSpecial


class CreatEnseignement(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model = Enseignement


class CreatPriere(CreateView):
    template_name = "evenements/creation_evenement.html"
    fields = "__all__"
    model = Priere

# liste tout les evenements
class ListEvents(ListView):
    model = Agape
    template_name = "evenements/liste_activites.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['culte'] = Culte.objects.all()
        context['culte_special'] = CulteSpecial.objects.all()
        context['partage'] = Partage.objects.all()
        context['priere'] = Priere.objects.all()
        context['enseignement'] = Enseignement.objects.all()

        return context

class DetailEvents(DetailView):
    model = Agape
    template_name = "evenements/infos_evenement.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['culte'] = Culte.objects.all()
        context['culte_special'] = CulteSpecial.objects.all()
        context['partage'] = Partage.objects.all()
        context['priere'] = Priere.objects.all()
        context['enseignement'] = Enseignement.objects.all()

        return context