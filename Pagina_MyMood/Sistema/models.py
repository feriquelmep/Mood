from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Tabla Persona
class Persona(models.Model):
    usuario=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    nombreCompleto=models.CharField(max_length=30)
    correoElectronico=models.EmailField(max_length=30)
    SEXOS=(('F','Femenino'),('M','Masculino'))
    sexo=models.CharField(max_length=1,choice=SEXOS, default='M')
    direccion=models.CharField(max_length=25)
    pais=models.CharField(max_length=25)
    tipoPersona=models.CharField(max_length=50, default='Usuario')


