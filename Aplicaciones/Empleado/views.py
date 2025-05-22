#importando el modelo cargo
from .models import Empleado
from django.shortcuts import render, redirect
from django.contrib import messages
def inicio(request):
    listadoEmpleado=Empleado.objects.all()
    return render(request,"inicioem.html",{'empleado':listadoEmpleado})

def nuevoEmpleado(request):
    return render(request,"nuevoEmpleado.html")
#Almacenando los datos de cargo en la Bdd
def guardarEmpleado(request):
    nombre = request.POST["nombre"]
    ubicacion = request.POST["ubicacion"]
    telefono = request.POST["telefono"]
    nuevoEmpleado=Empleado.objects.create(
            nombre=nombre,
            ubicacion=ubicacion,
            telefono=telefono,
        )
    #mensaje de confirmacion
    messages.success(request,"Empleado guardado exitosamente")
    return redirect('inicioem')
def eliminarEmpleado(request,id):
    empleadoEliminar = Empleado.objects.get(id=id)
    empleadoEliminar.delete()
    messages.success(request,"Empleado ELIMINADO exitosamente")
    return redirect('inicioem')

#editar
def editarEmpleado(request,id):
    empleadoEditar=Empleado.objects.get(id=id)
    return render(request,"editarEmpleado.html",{'empleadoEditar':empleadoEditar})

def procesarEdicionEmpleado(request):
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    ubicacion = request.POST["ubicacion"]
    telefono = request.POST["telefono"]
    empleado=Empleado.objects.get(id=id)
    empleado.nombre=nombre
    empleado.ubicacion=ubicacion
    empleado.telefono=telefono
    empleado.save()
    #mensaje de confirmacion
    messages.success(request,"Empleado ACTUALIZADO exitosamente")
    return redirect('inicioem')