# Generated by Django 5.1.4 on 2025-01-20 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='adresse',
            field=models.CharField(max_length=250, null=True, verbose_name='adresse'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='specialite',
            field=models.CharField(max_length=250, verbose_name='specialite'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=250, verbose_name='telephone'),
        ),
    ]
