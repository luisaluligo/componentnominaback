from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.tiponovedad import Tiponovedad
from authApp.serializers.tipoNovedadSerializer import TipoNovedadSerializer

class TipoNovedadCreateView(generics.CreateAPIView):
  queryset = Tiponovedad.objects.all()
  serializer_class= TipoNovedadSerializer
  permission_classes = (IsAuthenticated,)
 
  def post(self, request, *args, **kwargs):
       token = request.META.get('HTTP_AUTHORIZATION')[7:]
       tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
       valid_data = tokenBackend.decode(token, verify=False)
       return Response(request.data['tipo_novedad'].user)
       if valid_data['user_id'] != int(request.data['user']):
              stringResponse = {'detail': 'Unauthorized Request'}
              return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

       serializer = TipoNovedadSerializer(data=request.data['tiponovedad_data'])
       serializer.is_valid(raise_exception = True)
       serializer.save()
       
       return Response(serializer.data, status=status.HTTP_201_CREATED)