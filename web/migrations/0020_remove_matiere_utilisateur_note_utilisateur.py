# Generated by Django 4.2.1 on 2023-06-09 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0019_alter_matiere_utilisateur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matiere',
            name='utilisateur',
        ),
        migrations.AddField(
            model_name='note',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
