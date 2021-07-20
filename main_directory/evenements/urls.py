from django.urls import path
from .views import Index, NewEvent, CreatAgape, CreatCulte, CreatCulteSpecial, \
    CreatEnseignement, CreatPriere, CreatPartage, ListEvents, DetailEvents


urlpatterns = [
    # page d'accueil
    path('', Index.as_view(), name='acceuil'),
    # vue de creation
    path('evenement/nouveau', NewEvent.as_view(), name='ajout__event'),
    # formulaire de creations
    path('evenement/nouveau/agape', CreatAgape.as_view(), name='ajout__agape'),
    path('evenement/nouveau/culte', CreatCulte.as_view(), name='ajout__culte'),
    path('evenement/nouveau/cultespecial', CreatCulteSpecial.as_view(), name='ajout__cultespecial'),
    path('evenement/nouveau/enseignement', CreatEnseignement.as_view(), name='ajout__enseignement'),
    path('evenement/nouveau/priere', CreatPriere.as_view(), name='ajout__priere'),
    path('evenement/nouveau/partage', CreatPartage.as_view(), name='ajout__partage'),
    # listing
    path('evenement/', ListEvents.as_view(), name='liste_activites'),
    # details
    path('evenement/detail/<int:pk>', DetailEvents.as_view(), name="evenement-detail"),
]
