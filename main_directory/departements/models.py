from django.db import models

# Create your models here.

# lister de departements
class DepartementSorte(models.Model):
    nom = models.CharField(
        max_length=50,
        verbose_name="nom du departement",
    )

    def __str__(self):
        return self.nom

