# Generated by Django 4.2.1 on 2023-06-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_remove_matiere_utilisateur_note_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='lieu_de_naissance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
