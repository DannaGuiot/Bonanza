# Generated by Django 5.0.7 on 2024-08-14 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0029_remove_compra_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='estado',
        ),
    ]
