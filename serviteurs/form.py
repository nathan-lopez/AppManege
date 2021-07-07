# pour le model de formulaire
from django.forms import ModelForm, DateInput
from .models import Serviteurs
# from django.contrib.admin import widgets


class Datenput(DateInput):
    input_type = "date"

# pour la mise à jour de tout les informations d'un serviteurs
class Upadatallinfos(ModelForm):
    class Meta:
        model = Serviteurs
        fields = '__all__'
        widgets = {
            "date_de_naissance": Datenput()
        }
