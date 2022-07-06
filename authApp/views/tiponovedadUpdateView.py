from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from django.forms.models import model_to_dict

from authApp.models.tiponovedad import Tiponovedad
from authApp.serializers.tipoNovedadSerializer import TipoNovedadSerializer

class TiponovedadUpdateView(generics.UpdateAPIView):
     queryset = Tiponovedad.objects.all()
     serializer_class= TipoNovedadSerializer
     permission_classes = (IsAuthenticated,)

     def put(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        pk = kwargs["pk"]
        instance = Tiponovedad.objects.get(pk=pk)
        serializer = TipoNovedadSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, validated_data=request.data)
        return Response(model_to_dict(instance), status=status.HTTP_201_CREATED)

        
       