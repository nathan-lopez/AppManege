from django.db import models
# pour formater l'url
from django.shortcuts import reverse
import os

def renommage(instance, nom):
    nom_fichier = os.path.splitext(nom)[0] # on retire l'extension
    return "{}-{}".format(instance.id, nom_fichier)

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
    doc = models.ImageField(blank=True, null=True, upload_to=renommage, verbose_name=f"photo de {prenom}")
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


        # Model Save override
    def save(self, *args, **kwargs):
        if self.id is None:
            saved_document = self.doc
            self.doc = None
            super(Serviteurs, self).save(*args, **kwargs)
            self.doc = saved_document
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

            super(Serviteurs, self).save(*args, **kwargs)

    # obtenir les information par serviteurs
    def get_absolute_url(self):
        """Returne un url propres à chaque serviteur"""
        return reverse('serviteur-detail', kwargs={'pk': self.pk})
