from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from django.forms.models import model_to_dict

from authApp.serializers.empleadoSerializer import EmpleadoSerializer
from authApp.models.empleado import Empleado


class EmpleadoUpdateView(generics.UpdateAPIView):

    def put(self, request, *args, **kwargs):

        pk = kwargs["pk"]
        instance = Empleado.objects.get(pk=pk)
        serializer = EmpleadoSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, validated_data=request.data)

        return Response(model_to_dict(instance), status=status.HTTP_201_CREATED)
