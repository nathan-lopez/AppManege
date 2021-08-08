from django.shortcuts import render
from django.views.generic import ListView
from serviteurs.models import Serviteurs

def info_departement(request):
    return render(
        request,
        'departements/info_departement.html',
        context=None
    )


class Serviteurs_par_departement(ListView):
    model = Serviteurs
    template_name = "departements/liste_departement.html"

