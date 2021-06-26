from django.urls import path
from .views import Allserviteurs, Detailserviteur

urlpatterns = [
    path('', Allserviteurs.as_view(), name='serviteur-liste'),
    path('serviteurs/<int:pk>', Detailserviteur.as_view(), name='serviteur-detail'),
]
