from django.db.models import fields
from authApp.models.novedad import Novedad
from authApp.models.tiponovedad import Tiponovedad
from authApp.serializers.nominaSerializer import NominaSerializer
from rest_framework import serializers

class NovedadSerializer(serializers.ModelSerializer):
    codigo_nom = NominaSerializer(read_only=True)

    class Meta:
        model = Novedad
        fields = ['codigo_nov','codigo_nom','codigo_tipnov','valor_nov']

    
    def create(self, validated_data):
        novedadInstance = Novedad.objects.create(**validated_data)
        return novedadInstance
    
    def update(self, instance, novedadInstance,validated_data):
       
        novedadInstance.codigo_tipnov = validated_data.get('codigo_tipnov', instance.codigo_tipnov)
        novedadInstance.valor_nov = validated_data.get('valor_nov', instance.valor_nov)
        novedadInstance.save()
        return novedadInstance

    def to_representation(self, obj):
        novedad =Novedad.objects.get(codigo_nov=obj.codigo_nov)
        tiponovedad=Tiponovedad.objects.get(codigo_tipnov=obj.codigo_tipnov)
        return { 
                    'codigo_nov' : novedad.codigo_nov,
                    'tiponovedad':{ 'codigo_emp' : tiponovedad.codigo_tipnov,
                                   'nombre_tipnov' : tiponovedad.nombre_tipnov
                               },
                    'valor_nov':   novedad.valor_nov,
                  
              
               }
    