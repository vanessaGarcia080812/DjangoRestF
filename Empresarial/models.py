from django.db import models  # type: ignore
from django.core.validators import MaxValueValidator,MinValueValidator # type: ignore
from django.utils import timezone # type: ignore
from django.db import models # type: ignore
from django.contrib.auth.hashers import make_password, check_password # type: ignore
from django.contrib.auth.models import Permission # type: ignore
from django.contrib.auth.hashers import check_password as django_check_password # type: ignore
from django.core.validators import MaxValueValidator,MinValueValidator # type: ignore
from django.utils import timezone # type: ignore
from django.utils.timezone import timedelta # type: ignore


class Empresa(models.Model):
    nit = models.CharField(max_length=50, primary_key=True)
    razon_social = models.CharField(max_length=100) 
    telefono_entidad = models.CharField(max_length=15) 
    correo_entidad = models.EmailField() 
    imagen=models.ImageField(upload_to='photos')

    def __str__(self):
        return self.razon_social


class Empleado(models.Model):
    # estado_civil=[
    #     ('SOLTERO', 'Soltero/a'),
    #     ('CASADO', 'Casado/a'),
    #     ('DIVORCIADO', 'Divorciado/a'),
    #     ('VIUDO', 'Viudo/a'),
    # ]
    # tipo_documento=[
    #     ('Cc', 'Cedula de ciudadania'),
    #     ('Ce', 'Cedula de extrangeria'),
    #     ('Passpor', 'Pasaporte'),
    # ]
    # genero=[
    #     ('M', 'Masculino'),
    #     ('F', 'Femenino'),
    #     ('O', 'Otro'),
    #     ('P', 'Prefiero no decir'),
    # ]
    # nivel_riesgo=[
    #     ('1', 'Nivel 1'),
    #     ('2', 'Nivel 2'),
    #     ('3', 'Nivel 3'),
    #     ('4', 'Nivel 4'),
    #     ('5', 'Nivel 5'), 
    # ]

    numero_identificacion = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, blank=True, null=True)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30, blank=True, null=True)
    estado_civil = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    celular = models.CharField(max_length=10)
    genero = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    fecha_exp_documento = models.DateField()
    fecha_ingreso = models.DateField(null=True)
    nivel_riesgo=models.CharField(max_length=10,null=True)
    salario=models.FloatField(validators=[MinValueValidator(1300000)],null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,blank=True, null=True) 
    imagen=models.ImageField(upload_to='photos')

    def __str__(self):
        return f'{self.primer_nombre} {self.primer_apellido} - {self.numero_identificacion}'



class Usuarios(models.Model):
    id_rol=[
        ('Contador', 'Contador'),
        ('Auxiliar Contable', 'Auxiliar Contable'),
        ('RRHH', 'RRHH'),
        ('Empleado General', 'Empleado General'),
    ]

    usuario = models.ForeignKey(Empleado, on_delete=models.CASCADE) 
    intentos = models.IntegerField(default=0)
    estado_u = models.BooleanField(default=False)
    contrasena = models.CharField(max_length=88,null=True)
    id_rol= models.CharField(max_length=30) 
    
    def set_password(self, raw_password):
        self.contrasena = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return django_check_password(raw_password, self.contrasena)
    
class PasswordResetRequest(models.Model):
    usuario = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(null=True)

    used = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Es un nuevo objeto, establece la fecha de expiración
            self.expires_at = self.created_at + timedelta(minutes=15)
        super().save(*args, **kwargs)

    
class Calculos(models.Model):
    documento = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    salud = models.FloatField(validators=[MinValueValidator(0.0)],null=True)
    pension = models.FloatField(validators=[MinValueValidator(0.0)],null=True)
    arl = models.FloatField(validators=[MinValueValidator(0.0)],null=True)
    transporte = models.FloatField(validators=[MinValueValidator(0.0)],null=True)
    salarioBase = models.FloatField(validators=[MinValueValidator(0.0)],null=True)
    cajaCompensacion = models.FloatField(validators=[MinValueValidator(0.0)],null=True)
    sena = models.FloatField(null=True, validators=[MinValueValidator(0.0)], default=0.0)
    icbf = models.FloatField(null=True, validators=[MinValueValidator(0.0)], default=0.0)
    fecha_calculos = models.DateField(null=True)
    cesantias = models.FloatField(validators=[MinValueValidator(0.0)],null=True)
    interesCesantias = models.FloatField(validators=[MinValueValidator(0.0)],null=True)
    vacaciones = models.FloatField(validators=[MinValueValidator(0.0)],null=True)
    dias_vacaciones = models.FloatField(validators=[MinValueValidator(0.0)],null=True)
    HorasExDiu=models.IntegerField(blank=True,null=True)
    HorasExNoc=models.IntegerField(blank=True,null=True)
    HorasExFestivaDiu=models.IntegerField(blank=True,null=True)
    HorasExFestivaNoc=models.IntegerField(blank=True,null=True)
    recargoDiuFes=models.IntegerField(blank=True,null=True)
    recargoNoc=models.IntegerField(blank=True,null=True)
    recargoNocFest=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f'{self.documento} - {self.fecha_calculos}'
    
    
    
class Novedades(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_novedad=models.DateField(null=True,)
    HorasExDiu=models.IntegerField(validators=[MaxValueValidator(48),MinValueValidator(0)],blank=True,null=True)
    HorasExNoc=models.IntegerField(validators=[MaxValueValidator(48),MinValueValidator(0)],blank=True,null=True)
    HorasExFestivaDiu=models.IntegerField(validators=[MaxValueValidator(48),MinValueValidator(0)],blank=True,null=True)
    HorasExFestivaNoc=models.IntegerField(validators=[MaxValueValidator(48),MinValueValidator(0)],blank=True,null=True)
    recargoDiuFes=models.IntegerField(blank=True,null=True)
    recargoNoc=models.IntegerField(blank=True,null=True)
    recargoNocFest=models.IntegerField(blank=True,null=True)