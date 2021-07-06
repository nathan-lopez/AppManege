from django.db import models


class Evenement(models.Model):
    # information general sur l'evenement
    date = models.DateTimeField(verbose_name="heure et date de l'evenement ")
    theme = models.CharField(max_length=200)
    # le media de l'evenements
    fichier = models.FileField(blank=True, null=True, verbose_name='photos ou videos de l\' evenements')
    # information particulier
    moderateur = models.CharField(max_length=50)
    predicateur = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True


class Agape(Evenement):
    # retirer le champs qui n'on rien a avoir avec ce modele
    moderateur = None
    predicateur = None
    theme = None
    # pour le media
    lieu = models.TextField('lieu de l\'agape')
    # pour le media
    fichier = models.FileField(blank=True, null=True, verbose_name='photos ou videos de l\' evenements')

    def __str__(self):
        return self.lieu


class Culte(Evenement):

    resume_predication = models.TextField(verbose_name='resume de la predication')

    def __str__(self):
        return self.theme


class CulteSpecial(Culte):

    predicateur2 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='deuxième predicateur',
    )
    service_prophetique = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='service prophetique',
    )
    service_prophetique2 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='deuxieme intervenant aux service prophetique',
    )

    def __str__(self):

        return self.theme


class Enseignement(Evenement):
    # champs non pertinant
    predicateur = None
    moderateur = None

    # champ pertinant
    # theme, heure, fichier
    corp_enseignement = models.TextField(verbose_name='corp de l\' enseignement')
    enseignant = models.CharField(max_length=50, verbose_name='nom de l\'enseignant')

    def __str__(self):
        return self.theme


class Partage(Evenement):
    # champs non pertinant
    predicateur = None

    def __str__(self):
        return self.theme


class Priere(Evenement):
    # champs non pertinants
    predicateur = None
    exhortation = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name="personne en charge de l'exhoration",
    )

    def __str__(self):
        return self.theme
