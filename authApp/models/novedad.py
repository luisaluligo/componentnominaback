from django.db import models
from .nomina import Nomina
from .tiponovedad import Tiponovedad

class Novedad(models.Model):
    codigo_nov = models.BigAutoField(primary_key=True)
    codigo_nom = models.ForeignKey(Nomina, models.DO_NOTHING, db_column='codigo_nom')
    codigo_tipnov = models.ForeignKey(Tiponovedad, models.DO_NOTHING, db_column='codigo_tipnov')
    valor_nov = models.BigIntegerField()

    class Meta:
        db_table = 'novedad'
        
    




