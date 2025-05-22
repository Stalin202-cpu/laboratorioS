#importando el modelo cargo
from .models import Empleado
from django.shortcuts import render, redirect
from django.contrib import messages
def inicio(request):
    listadoEmpleado=Empleado.objects.all()
    return render(request,"inicioem.html",{'empleado':listadoEmpleado})