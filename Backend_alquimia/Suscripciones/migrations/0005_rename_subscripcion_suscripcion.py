# Generated by Django 5.1.5 on 2025-01-31 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Suscripciones', '0004_rename_subscripcioncliente_subscripcion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscripcion',
            new_name='Suscripcion',
        ),
    ]
