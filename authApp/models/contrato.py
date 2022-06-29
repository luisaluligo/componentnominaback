from django.db import models
from .empleado import Empleado

class Contrato(models.Model):
    codigo_con = models.BigAutoField(primary_key=True)
    codigo_emp = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='codigo_emp' )
    cargo_cont = models.CharField(max_length=250)
    salario_con = models.BigIntegerField()
    fechainicio_con = models.DateField(blank=True, null=True)
    fechafin_con = models.DateField(blank=True, null=True)
    tipo_con = models.CharField(max_length=25)

    class Meta:
       
        db_table = 'contrato'