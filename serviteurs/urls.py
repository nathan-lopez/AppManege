from django.urls import path
from .views import Allserviteurs, Detailserviteur, CreeServiteur, ModifierServiteur, \
    SuprimerServiteur, InterServiteur

urlpatterns = [
    path('', Allserviteurs.as_view(), name='serviteur-liste'),
    path('serviteurs/<int:pk>', Detailserviteur.as_view(), name='serviteur-detail'),
    path('serviteurs/nouveau/', CreeServiteur.as_view(), name='serviteur-nouveau'),
    path('serviteurs/modification/<int:pk>', ModifierServiteur.as_view(), name='serviteur-modification'),
    path('serviteurs/suppression/<int:pk>', SuprimerServiteur.as_view(), name='serviteur-suppression'),
    path('servieurs/upload_or_delete', InterServiteur.as_view(), name='serviteur-delete_uploade'),
]
