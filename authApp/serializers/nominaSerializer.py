from django.db.models import fields
from authApp.models.nomina import Nomina,ESTADOS_CHOICES
from authApp.models.empleado import Empleado
from authApp.models.novedad import Novedad
from authApp.models.tiponovedad import Tiponovedad
from authApp.serializers.empleadoSerializer import EmpleadoSerializer
from rest_framework import serializers

class NominaSerializer(serializers.ModelSerializer):
    estado_nom=serializers.ChoiceField(choices=ESTADOS_CHOICES)
    class Meta:
        model = Nomina
        fields = ['codigo_nom','codigo_emp','estado_nom','fechainicio_nom','fechafin_nom','salariobase_nom','salariodevengo_nom','salariodeduccion_nom','salariototal_emp']
           
    
     
    def create(self,validated_data):
        nominaInstancia=  Nomina.objects.create(**validated_data)
        return nominaInstancia

    def update(self,instance,validate_data):
        instance.estado_nom = validate_data.get("estado_nom",instance.estado_nom)
        instance.fechainicio_nom = validate_data.get("fechainicio_nom",instance.fechainicio_nom)
        instance.fechafin_nom = validate_data.get("fechafin_nom",instance.fechafin_nom)
        instance.salariobase_nom = validate_data.get("salariobase_nom",instance.salariobase_nom)
        instance.salariodevengo_nom = validate_data.get("salariodevengo_nom",instance.salariodevengo_nom)
        instance.salariodeduccion_nom = validate_data.get("salariodeduccion_nom",instance.salariodeduccion_nom)
        instance.save()
        return instance
    
    def to_representation(self, obj):
        nomina = Nomina.objects.get(codigo_nom=obj.codigo_nom)
        empleado =Empleado.objects.get(codigo_emp=obj.codigo_emp)
        novedad =Novedad.objects.get(codigo_nom=obj.codigo_nom,codigo_emp=obj.codigo_emp)
        tiponovedad=Tiponovedad.objects.get(codigo_tipnov=obj.codigo_tipnov)
        return { 
                    'codigo_nom' : nomina.codigo_nom,
                    'empleado':{ 'codigo_emp' : empleado.codigo_emp,
                                 'nombre_emp' : empleado.nombre_emp
                               },
                    'estado':   nomina.estado_nom,
                    'fechainicio_nom' : nomina.fechainicio_nom,
                    'fechafin_nom':  nomina.fechafin_nom, 
                    
                    'novedad':{ 'codigo_nov' : novedad.codigo_nov,
                                'nombre_tipnov':tiponovedad.nombre_tipnov,
                                'valor_nov' : novedad.valor_nov
                               },
                    'salariobase_nom' :  nomina.salariobase_nom,
                    'salariodevengo_nom' :  nomina.salariodevengo_nom,
                    'salariodeduccion_nom' :  nomina.salariodeduccion_nom,
                    'salariototal_emp':  nomina.salariototal_emp
              
               }
    
    
