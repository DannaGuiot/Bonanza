# Generated by Django 4.1.3 on 2024-07-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_categoria_libro_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('presentacion', models.CharField(max_length=100)),
                ('unidad_de_medida', models.CharField(max_length=20)),
            ],
        ),
    ]
