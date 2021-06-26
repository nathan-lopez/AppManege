from django.db import models
# pour formater l'url
from django.shortcuts import reverse


class Serviteurs(models.Model):
    # mes constante
    RESPONSABLE = (
        ('P', 'Père'),
        ('M', 'Mère'),
        ('T', 'Tutreur'),
    )
    STATUS_SERVICE = (
        ('S', 'Suspendu'),
        ('O', 'En observation'),
        ('B', 'conduite parfaite'),
    )
    # information personnelle
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    post_nom = models.CharField(max_length=100)
    date_de_naissance = models.DateField("date de naissance")
    photo = models.ImageField(blank=True, null=True)
    contact = models.CharField("numero de contact", max_length=15, help_text="ex : +243", blank=True, null=True)
    reseau = models.CharField("numero reseau sociaux", max_length=15, blank=True, null=True)
    adresse = models.TextField(help_text=" Lubumbashi/C. kenya/Av. circulaire/n°303")

    # Personne à contacter en cas d'urgence
    nomc = models.CharField("nom complet", max_length=250, null=True, blank=True)
    contactC = models.CharField("numero de contact de la personne à contacter", max_length=15)
    degret = models.CharField(
        verbose_name="degré de parenté",
        max_length=1,
        choices=RESPONSABLE,
        default='P',
        help_text="preciser le degré de parenté",
    )
    adresseC = models.TextField(help_text=" Lubumbashi/C. kenya/Av. circulaire/n°303")

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

    # valuer de retour
    def __str__(self):
        return f'{self.prenom} {self.post_nom} {self.nom}'

    # obtenir les information par serviteurs
    def get_absolute_url(self):
        """Returne un url propres à chaque serviteur"""
        return reverse('serviteur-detail', kwargs={'pk': self.pk})
