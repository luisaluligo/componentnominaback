from django.db.models import fields
from authApp.models.tiponovedad import Tiponovedad
from rest_framework import serializers

class TipoNovedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiponovedad
        fields = ['codigo_tipnov','nombre_tipnov','tipoconcepto_tipnov','valorbase_tipnov']
        
    def create(self, validated_data):
        tipoNovedadInstance = Tiponovedad.objects.create(**validated_data)
        return tipoNovedadInstance
    
    def update(self, instance, tipoNovedadInstance,validated_data):
       
        tipoNovedadInstance.codigo_tipnov = validated_data.get('codigo_tipnov', instance.codigo_tipnov)
        tipoNovedadInstance.nombre_tipnov = validated_data.get('nombre_tipnov', instance.nombre_tipnov)
        tipoNovedadInstance.tipoconcepto_tipnov = validated_data.get('tipoconcepto_tipnov', instance.tipoconcepto_tipnov)
        tipoNovedadInstance.valorbase_tipnov = validated_data.get('valorbase_tipnov', instance.valorbase_tipnov)
        tipoNovedadInstance.save()
        return tipoNovedadInstance