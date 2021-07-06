from django.contrib import admin
from .models import Agape,Culte, CulteSpecial, Enseignement, Priere, Partage

# Register your models here.

admin.site.register(Agape)
admin.site.register(Culte)
admin.site.register(CulteSpecial)
admin.site.register(Enseignement)
admin.site.register(Partage)
admin.site.register(Priere)
