# Generated by Django 3.2.3 on 2021-06-26 03:30

from django.db import migrations, models
import serviteurs.models


class Migration(migrations.Migration):

    dependencies = [
        ('serviteurs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviteurs',
            name='photo',
        ),
        migrations.AddField(
            model_name='serviteurs',
            name='doc',
            field=models.ImageField(blank=True, null=True, upload_to=serviteurs.models.renommage, verbose_name='photo de <django.db.models.fields.CharField>'),
        ),
    ]