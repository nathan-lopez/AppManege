from django.db import models

# Create your models here.

class Evenement(models.Model):
    TYPE = (
        ('agape', 'agape'),
        ('culte', 'culte'),
        ('culte special', 'culte special'),
        ('enseignement', 'enseignement'),
        ('prière', 'prière'),
        ('partage', 'partage'),
    )
    # champ obligatoire
    date = models.DateTimeField(verbose_name="heure et date de l'evenement ")
    type = models.CharField(
        max_length=100,
        choices=TYPE,
        default="culte",
        help_text="le type de l'evenement",
    )
    if type == "culte":
        prenom = models.CharField(max_length=100)
        nom = models.CharField(max_length=100)
    else:
        adresseC = models.TextField(help_text=" Lubumbashi/C. kenya/Av. circulaire/n°303")

    def __str__(self):
        return "hello"