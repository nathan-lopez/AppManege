from django.db import models
# pour formater l'url
from django.shortcuts import reverse
# import os


class Serviteurs(models.Model):
    # mes constante
    RESPONSABLE = (
        ('Père', 'Père'),
        ('Mère', 'Mère'),
        ('Tuteur', 'Tutreur'),
    )
    STATUS_SERVICE = (
        ('S', 'Suspendu'),
        ('O', 'En observation'),
        ('B', 'conduite parfaite'),
    )
    GENRE = (
        ('Servante', 'Servante'),
        ('Serviteur', 'Serviteur'),
    )
    # information personnelle
    prenom = models.CharField(max_length=100)
    post_nom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    genre = models.CharField(
        verbose_name='Genre',
        max_length=10,
        choices=GENRE,
        default='Servante',
    )
    date_de_naissance = models.DateField("date de naissance")
    doc = models.ImageField(
        blank=True,
        null=True,
        upload_to='photo',
    )
    contact = models.CharField("numero de contact", max_length=15, help_text="ex : +243", blank=True, null=True)
    reseau = models.CharField("numero reseau sociaux", max_length=15, blank=True, null=True)
    adresse = models.CharField(max_length=350, help_text=" Lubumbashi/C. kenya/Av. circulaire/n°303")

    # Personne à contacter en cas d'urgence
    nom_responsable = models.CharField("nom complet", max_length=250, null=True, blank=True)
    contactC = models.CharField("numero de contact de la personne à contacter", max_length=15)
    degret = models.CharField(
        verbose_name="Degré de parenté",
        max_length=6,
        choices=RESPONSABLE,
        default='Père',
    )
    adresseC = models.CharField(max_length=350, help_text=" Lubumbashi/C. kenya/Av. circulaire/n°303")


    # relatif à la conduite et au service
    # service
    # nombre de sercice par ans
    # culte et date

    # conduite
    status = models.CharField(
        max_length=1,
        choices=STATUS_SERVICE,
        blank=True,
        default='B',
        help_text='resumé de la conduite d\' un serviteur',
    )

    # obtenir les information par serviteurs
    def get_absolute_url(self):
        """Returne un url propres à chaque serviteur"""
        return reverse('serviteur-detail', kwargs={'pk': self.pk})
