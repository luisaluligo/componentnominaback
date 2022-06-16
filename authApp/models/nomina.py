from django.db import models
from .empleado import Empleado

ESTADOS_CHOICES = [('liquidada','liquidada'),('pre-liquidada','pre-liquidada')]

class Nomina(models.Model):
    codigo_nom = models.BigAutoField(primary_key=True)
    codigo_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='codigo_emp')
    estado_nom = models.CharField(choices=ESTADOS_CHOICES, max_length=20)
    fechainicio_nom = models.DateField()
    fechafin_nom = models.DateField()
    salariobase_nom = models.BigIntegerField(blank=True, null=True)
    salariodeduccion_nom = models.BigIntegerField(blank=True, null=True)
    salariodevengo_nom = models.BigIntegerField(blank=True, null=True)
    salariototal_emp = models.BigIntegerField(blank=True, null=True)

  
    class Meta:
        db_table = 'nomina'
        unique_together = (('codigo_nom', 'codigo_emp'),)
