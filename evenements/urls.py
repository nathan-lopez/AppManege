from django.urls import path
from .views import Index, NewEvent, CreatAgape, CreatCulte, CreatCulteSpecial, \
    CreatEnseignement, CreatPriere, CreatPartage, ListAgape, ListCulte, ListCulteSpecial, ListEnseignement, \
    ListPriere, ListPartage

urlpatterns = [
    path('', Index.as_view(), name='acceuil'),
    path('evenement/nouveau', NewEvent.as_view(), name='ajout__event'),
    path('evenement/nouveau/agape', CreatAgape.as_view(), name='ajout__agape'),
    path('evenement/nouveau/culte', CreatCulte.as_view(), name='ajout__culte'),
    path('evenement/nouveau/cultespecial', CreatCulteSpecial.as_view(), name='ajout__cultespecial'),
    path('evenement/nouveau/enseignement', CreatEnseignement.as_view(), name='ajout__enseignement'),
    path('evenement/nouveau/priere', CreatPriere.as_view(), name='ajout__priere'),
    path('evenement/nouveau/partage', CreatPartage.as_view(), name='ajout__partage'),
    # listing
    path('evenement/', ListAgape.as_view(), name='listing'),
    path('evenement/', ListCulte.as_view(), name='listing'),
    path('evenement/', ListCulteSpecial.as_view(), name='listing'),
    path('evenement/', ListEnseignement.as_view(), name='listing'),
    path('evenement/', ListPriere.as_view(), name='listing'),
    path('evenement/', ListPartage.as_view(), name='listing'),
]
