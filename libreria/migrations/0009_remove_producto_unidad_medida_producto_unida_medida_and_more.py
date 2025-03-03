# Generated by Django 4.1.3 on 2024-07-24 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0008_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='unidad_medida',
        ),
        migrations.AddField(
            model_name='producto',
            name='unida_medida',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='libreria.unidadmedida', verbose_name='UnidadMedida'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='libreria.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='libreria.marca', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='presentacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='libreria.presentacion', verbose_name='Presentacion'),
        ),
    ]
