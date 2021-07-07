from django.urls import path
from .views import Allserviteurs, Detailserviteur, CreeServiteur, ModifierServiteur, SuprimerServiteur

urlpatterns = [
    path('', Allserviteurs.as_view(), name='serviteur-liste'),
    path('serviteurs/<int:pk>', Detailserviteur.as_view(), name='serviteur-detail'),
    path('serviteurs/nouveau/', CreeServiteur.as_view(), name='serviteur-nouveau'),
    path('serviteurs/modification/<int:pk>', ModifierServiteur.as_view(), name='serviteur-modification'),
    path('serviteurs/suppression/<int:pk>', SuprimerServiteur.as_view(), name='serviteur-suppression'),
]
