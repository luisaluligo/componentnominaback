from django.db import models


class Empleado(models.Model):
    codigo_emp = models.BigIntegerField(primary_key=True)
    nombre_emp = models.CharField(max_length=230)
    tipo_persona_emp = models.CharField(max_length=8, blank=True, null=True)
    estado_emp= models.CharField(max_length=230)
    
    
