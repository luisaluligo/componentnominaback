from authApp.models.novedad import Novedad
from authApp.serializers.novedadSerializer import NovedadSerializer
from django.conf import settings
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend


class NovedadListView(generics.ListAPIView):

    queryset =  Novedad.objects.all()
    serializer_class=  NovedadSerializer
    serializer_class = (IsAuthenticated,)

    def get_query_set(self):

        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
            
        queryset = Novedad.objects.filter(cod_nom=self.kwargs['cod_nom'],cod_emp=self.kwargs['cod_emp'] )
       
        
        return queryset

