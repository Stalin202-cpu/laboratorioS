# Configuracion de rutas especificas de la app empresas
from django.urls import path
from . import views

urlpatterns=[
    path('inicioem',views.inicio,name='inicioem'),
    path('nuevoEmpleado',views.nuevoEmpleado),
    path('guardarEmpleado',views.guardarEmpleado),
    path('eliminarEmpleado/<id>',views.eliminarEmpleado),
    path('editarEmpleado/<id>',views.editarEmpleado),
    path('procesarEdicionEmpleado',views.procesarEdicionEmpleado),
]