# Generated by Django 5.0.6 on 2024-06-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empresarial', '0018_calculos_horasexdiu_calculos_horasexfestivadiu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='estado_civil',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='genero',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nivel_riesgo',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='tipo_documento',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='id_rol',
            field=models.CharField(max_length=30),
        ),
    ]
