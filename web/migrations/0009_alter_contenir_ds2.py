# Generated by Django 4.2.1 on 2023-06-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_contenir_ds2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenir',
            name='DS2',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]