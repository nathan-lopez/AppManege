# pour le model de formulaire
from django.forms import ModelForm
from .models import Serviteurs


# pour la mise à jour de tout les informations d'un serviteurs
class Upadatallinfos(ModelForm):
    class Meta:
        model = Serviteurs
        fields = '__all__'