#importando el modelo cargo
from .models import Muestreo
from .models import Vinedo
from .models import Empleado
from django.shortcuts import render, redirect
from django.contrib import messages
def inicio(request):
    listadoMuestreo=Muestreo.objects.all()
    return render(request,"iniciomu.html",{'muestreo':listadoMuestreo})

def nuevoMuestreo(request):
    rempleados=Empleado.objects.all()
    lvinedos=Vinedo.objects.all()
    return render(request,"nuevoMuestreo.html",{'empleados':rempleados,'vinedos':lvinedos})
#Almacenando los datos de cargo en la Bdd
def guardarMuestreo(request):
    fecha = request.POST["fecha"]
    resultados = request.POST["resultados"]
    analistaid = request.POST["analista"]
    analista=Empleado.objects.get(id=analistaid)
    vinedoid = request.POST["vinedo"]
    vinedo=Vinedo.objects.get(id=vinedoid)
    nuevoMuestreo=Muestreo.objects.create(
            fecha=fecha,
            resultados=resultados,
            analista=analista,
            vinedo=vinedo,
        )
    #mensaje de confirmacion
    messages.success(request,"Muestreo guardado exitosamente")
    return redirect('iniciomu')

def eliminarMuestreo(request,id):
    muestreoEliminar = Muestreo.objects.get(id=id)
    muestreoEliminar.delete()
    messages.success(request,"Muestreo ELIMINADO exitosamente")
    return redirect('iniciomu')

#editar
def editarMuestreo(request,id):
    muestreoEditar=Muestreo.objects.get(id=id)
    rempleados=Empleado.objects.all()
    lvinedos=Vinedo.objects.all()
    return render(request,"editarMuestreo.html",{'muestreoEditar':muestreoEditar, 'empleados':rempleados,'vinedos':lvinedos})

def procesarEdicionMuestreo(request):
    id=request.POST["id"]
    fecha = request.POST["fecha"]
    resultados = request.POST["resultados"]
    analistaid = request.POST["analista"]
    analista=Empleado.objects.get(id=analistaid)
    vinedoid = request.POST["vinedo"]
    vinedo=Vinedo.objects.get(id=vinedoid)
    muestreo=Muestreo.objects.get(id=id)
    muestreo.fecha=fecha
    muestreo.resultados=resultados
    muestreo.analista= analista
    muestreo.vinedo= vinedo
    muestreo.save()
    #mensaje de confirmacion
    messages.success(request,"Muestreo ACTUALIZADO exitosamente")
    return redirect('iniciomu')
