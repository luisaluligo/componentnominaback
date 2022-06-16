from django.db import models

CONCEPTO_CHOICES = [('ingreso','ingreso'),('descuento','descuento')]

class Tiponovedad(models.Model):
    codigo_tipnov = models.BigAutoField(primary_key=True)
    nombre_tipnov = models.CharField(max_length=250)
    tipoconcepto_tipnov = models.CharField(choices= CONCEPTO_CHOICES,max_length=10)
    valorbase_tipnov = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tiponovedad'