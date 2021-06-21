from django.urls import path
from .views import Allserviteurs

urlpatterns = [
    path('', Allserviteurs.as_view(), name='serviteur-liste'),
]