from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.empleado import Empleado
from authApp.serializers.empleadoSerializer import EmpleadoSerializer


class EmpleadoGetView(generics.RetrieveAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)
