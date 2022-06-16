from django.db.models import fields
from authApp.models.contrato import Contrato
from rest_framework import serializers

class ContratoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contrato
    fields = ['cargo_cont','salario_con','fechainicio_con','fechafin_con','tipo_con']
    