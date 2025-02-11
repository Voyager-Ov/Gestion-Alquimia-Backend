# Generated by Django 5.1.5 on 2025-02-10 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Suscripciones', '0006_suscripcion_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='suscripcion',
            name='estado',
            field=models.CharField(choices=[('activa', 'Activa'), ('desactiva', 'Desactiva')], default=1, max_length=20, verbose_name='Estado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='suscripcion',
            name='tipo_suscripcion',
            field=models.CharField(choices=[('familiar', 'Familar'), ('individual', 'Individual'), ('pareja', 'Pareja'), ('alquimia', 'Alquimia')], max_length=20, verbose_name='Tipo de Suscripcion'),
        ),
    ]
