# Generated by Django 5.1.4 on 2025-01-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docteur', '0002_docteur_archive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docteur',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
