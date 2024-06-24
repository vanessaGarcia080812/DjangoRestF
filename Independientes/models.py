from django.db import models  # type: ignore
from django.contrib.auth.hashers import make_password, check_password  # type: ignore
from django.contrib.auth.models import Permission  # type: ignore
from django.contrib.auth.hashers import check_password as django_check_password  # type: ignore
from django.core.validators import MaxValueValidator,MinValueValidator  # type: ignore
from django.utils import timezone  # type: ignore
from django.utils.timezone import timedelta  # type: ignore
from rest_framework import serializers # type: ignore

# Create your models here.
class Independiente(models.Model):


    numero_identificacion = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, blank=True, null=True)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30, blank=True, null=True)
    estado_civil = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=50 )
    correo = models.EmailField(unique=True)
    celular = models.CharField(max_length=15)
    genero = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    fecha_exp_documento = models.DateField()
    imagen=models.ImageField(upload_to='photos')

    def __str__(self):
        return self.primer_nombre
    
class Calculos(models.Model):
    documento = models.ForeignKey(Independiente, on_delete=models.CASCADE)
    salud=models.FloatField(blank=True, null=True)
    pension=models.FloatField(blank=True,null=True)
    arl=models.FloatField(blank=True,null=True)
    salarioBase=models.FloatField(blank=True,null=True)
    cajaCompensacion=models.FloatField(blank=True,null=True)
    FSP=models.FloatField(blank=True,null=True)
    
class DatosCalculos(models.Model):

    documento = models.ForeignKey(Independiente, on_delete=models.CASCADE)
    salarioBase=models.FloatField(null=True, blank=True)
    ibc=models.FloatField(validators=[MaxValueValidator(100),MinValueValidator(40)],null=True)
    salud=models.FloatField( max_length=50, default=12.5)
    pension=models.FloatField(max_length=50, default=16)
    arl=models.FloatField(blank=True,null=True, max_length=25)
    CCF=models.FloatField(blank=True,null=True,  max_length=25)
    FSP=models.FloatField(blank=True,null=True,  max_length=25)
