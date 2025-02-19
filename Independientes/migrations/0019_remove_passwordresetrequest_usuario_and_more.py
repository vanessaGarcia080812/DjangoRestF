# Generated by Django 5.0.6 on 2024-06-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Independientes', '0018_alter_independiente_numero_identificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordresetrequest',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='datoscalculos',
            name='CCF',
            field=models.FloatField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='datoscalculos',
            name='FSP',
            field=models.FloatField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='datoscalculos',
            name='arl',
            field=models.FloatField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='estado_civil',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='genero',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='tipo_documento',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Novedades',
        ),
        migrations.DeleteModel(
            name='PasswordResetRequest',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
