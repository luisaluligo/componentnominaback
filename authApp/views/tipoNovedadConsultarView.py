from authApp.models.tiponovedad import Tiponovedad
from authApp.serializers.tipoNovedadSerializer import TipoNovedadSerializer
from django.conf import settings
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend


class TipoNovedadListView(generics.ListAPIView):
    serializer_class=  TipoNovedadSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        if valid_data['user_id'] != int(self.kwargs['user']):
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return  Tiponovedad.objects.all()
    