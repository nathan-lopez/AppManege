from django.shortcuts import render

# Create your views here.

def Liste_de_departement(request):

    return render(
        request,
        template_name="departements/liste_departement.html",
        context=None,
    )
