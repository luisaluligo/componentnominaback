from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.tiponovedad import Tiponovedad
from authApp.serializers.tipoNovedadSerializer import TipoNovedadSerializer

class TiponovedadUpdateView(generics.UpdateAPIView):
     queryset = Tiponovedad.objects.all()
     serializer_class= TipoNovedadSerializer
     permission_classes = (IsAuthenticated,)

     def update(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 
        return super().destroy(request, *args, **kwargs)

       