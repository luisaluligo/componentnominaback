from django.db.models import fields
from authApp.models.empleado import Empleado
from authApp.models.contrato import Contrato
from authApp.serializers.contratoSerializer import ContratoSerializer
from rest_framework import serializers


class EmpleadoSerializer(serializers.ModelSerializer):
    contrato = ContratoSerializer()

    class Meta:
        model = Empleado
        fields = ['codigo_emp', 'nombre_emp', 'tipo_persona_emp', 'estado_emp', 'contrato']

    def create(self, validated_data):
        contratoData = validated_data.pop('contrato')
        empleadoInstance = Empleado.objects.create(**validated_data)
        Contrato.objects.create(codigo_emp=empleadoInstance, **contratoData)
        return empleadoInstance

    def update(self, instance, validated_data):
        contratoData = validated_data.pop('contrato')
        instance.nombre_emp = validated_data.get("nombre_emp", instance.nombre_emp)
        instance.tipo_persona_emp = validated_data.get("tipo_persona_emp", instance.tipo_persona_emp)
        instance.estado_emp = validated_data.get("estado_emp", instance.estado_emp)
        instance.save()
        contrato = Contrato.objects.get(codigo_emp=instance.codigo_emp)
        contrato.cargo_cont = contratoData.get("cargo_cont", contrato.cargo_cont)
        contrato.salario_con = contratoData.get("salario_con", contrato.salario_con)
        contrato.fechainicio_con = contratoData.get("fechainicio_con", contrato.fechainicio_con)
        contrato.fechafin_con = contratoData.get("fechafin_con", contrato.fechafin_con)
        contrato.tipo_con = contratoData.get("tipo_con", contrato.tipo_con)
        contrato.save()

        return instance

    def to_representation(self, obj):
        empleado = Empleado.objects.get(codigo_emp=obj.codigo_emp)
        contrato = Contrato.objects.get(codigo_emp=obj.codigo_emp)
        return{
            'codigo_emp': empleado.codigo_emp,
            'nombre_emp': empleado.nombre_emp,
            'tipo_persona_emp': empleado.tipo_persona_emp,
            'estado_emp': empleado.estado_emp,
            'contrato': {
                'cargo_cont': contrato.cargo_cont,
                'salario_con': contrato.salario_con,
                'fechainicio_con': contrato.fechainicio_con,
                'fechafin_con': contrato.fechafin_con,
                'tipo_con': contrato.tipo_con
            }
        }
