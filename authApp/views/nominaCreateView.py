from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.nomina import Nomina
from authApp.serializers.nominaSerializer import NominaSerializer
from authApp.models.novedad import Novedad


class NominaCreateView(generics.CreateAPIView):
  
  serializer_class= NominaSerializer
  serializer_class = (IsAuthenticated,)
 
  def post(self, request, *args, **kwargs):
      
       
       token = request.META.get('HTTP_AUTHORIZATION')[7:]
       tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
       valid_data = tokenBackend.decode(token, verify=False)

       if valid_data['user_id'] != int(request.data['user_id']):
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

       nominaserializer = NominaSerializer(data=request.data['nomina_data'])
       nominaserializer.is_valid(raise_exception = True)
       nominaserializer.save()

      
       return Response("Nomina generada",status=status.HTTP_201_CREATED)


