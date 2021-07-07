# Generated by Django 3.2.3 on 2021-07-07 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serviteurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('post_nom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('Servante', 'Servante'), ('Serviteur', 'Serviteur')], default='Servante', max_length=10, verbose_name='Genre')),
                ('date_de_naissance', models.DateField(verbose_name='date de naissance')),
                ('lieu_de_naissance', models.CharField(max_length=50, verbose_name='lieu de naissance')),
                ('doc', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('contact', models.CharField(blank=True, help_text='ex : +243', max_length=15, null=True, verbose_name='numero de contact')),
                ('reseau', models.CharField(blank=True, max_length=15, null=True, verbose_name='numero reseau sociaux')),
                ('adresse', models.CharField(help_text=' Lubumbashi/C. kenya/Av. circulaire/n°303', max_length=350)),
                ('nom_responsable', models.CharField(blank=True, max_length=250, null=True, verbose_name='nom complet')),
                ('contactC', models.CharField(max_length=15, verbose_name='numero de contact de la personne à contacter')),
                ('degret', models.CharField(choices=[('Père', 'Père'), ('Mère', 'Mère'), ('Tuteur', 'Tutreur')], default='Père', max_length=6, verbose_name='Degré de parenté')),
                ('adresseC', models.CharField(help_text=' Lubumbashi/C. kenya/Av. circulaire/n°303', max_length=350)),
                ('poste', models.CharField(choices=[('President', 'President'), ('vice-precident', 'vice-precident'), ('secretaire', 'secretaire'), ('poste unique', 'poste unique')], default='poste unique', max_length=20)),
                ('status', models.CharField(blank=True, choices=[('suspendu', 'Suspendu'), ('parfaite', 'parfaite'), ('bonne', 'bonne'), ('irregulier', 'En observation')], default='bonne', help_text="resumé de la conduite d' un serviteur", max_length=10)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departements.departementsorte')),
            ],
        ),
    ]
