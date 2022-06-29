from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict

from authApp.serializers.empleadoSerializer import EmpleadoSerializer
from authApp.models.empleado import Empleado
from authApp.models.contrato import Contrato
from authApp.models.nomina import Nomina


class EmpleadoDeleteView(generics.RetrieveUpdateDestroyAPIView):

    def destroy(self, request, *args, **kwargs):
        serializer_class = EmpleadoSerializer(data=request.data)
        pk = kwargs["pk"]
        if Empleado.objects.filter(codigo_emp=pk).exists():
            instanceContrato = Contrato.objects.get(codigo_emp=pk)
            instanceEmpleado = Empleado.objects.get(pk=pk)
            if Nomina.objects.filter(codigo_emp=pk).exists():
                instanceNomina = Nomina.objects.get(codigo_emp=pk)
                self.perform_destroy(instanceNomina)
            self.perform_destroy(instanceContrato)
            self.perform_destroy(instanceEmpleado)

        else:
            return Response({'message': 'Empleado no existe en la base de datos'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Se eliminó el empleado correctamente'}, status=status.HTTP_200_OK)
