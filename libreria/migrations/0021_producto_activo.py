# Generated by Django 5.0.7 on 2024-08-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0020_remove_presentacion_estado_remove_marca_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
