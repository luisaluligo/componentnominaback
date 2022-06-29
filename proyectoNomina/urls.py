from authApp import views
from django.db import router
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('registrarEmpleado/', views.EmpleadoCreateView.as_view()),
    path('obtenerInfoEmpleado/<int:pk>', views.EmpleadoGetView.as_view()),
    path('infoPersonal/', views.EmpleadoDetailView.as_view()),
    path('editarEmpleado/<int:pk>/', views.EmpleadoUpdateView.as_view()),
    path('eliminarEmpleado/<int:pk>/', views.EmpleadoDeleteView.as_view()),
    path('crearNomina/', views.NominaCreateView.as_view()),
    path('consultarNomina/<int:user>/<int:pk>/', views.NominaDetailView.as_view()),
    path('editarNomina/<int:pk>/', views.NominaUpdateView.as_view()),
    path('consultarNovedades/<int:user>/<int:cod_nom>/<int:cod_emp>/', views.NovedadListView.as_view()),
    path('eliminarNovedad/<int:user>/<int:pk>/', views.NovedadDeleteView.as_view()),
    path('crearTipoNovedad/', views.TipoNovedadCreateView.as_view()),
    path('editarTipoNovedad/<int:user>/<int:pk>/', views.TiponovedadUpdateView.as_view()),
    path('consultarTipoNovedades/<int:user>/', views.TipoNovedadListView.as_view()),
]
