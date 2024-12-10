from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Componente, Colaborador, Sede
from .forms import CursoFormulario, ComponenteFormulario, SedeFormulario, ColaboradorFormulario
# Create your views here.

def inicio(request):
    return render(request,"myapp/index.html")

def componentes(request):
    query = request.GET.get("q")
    if query:
        componentes = Componente.objects.filter(nombre__icontains=query)
    else:
        componentes = Componente.objects.all()
    return render(request, "myapp/componentes.html", {"componentes": componentes})

def colaboradores(request):
    query = request.GET.get("q")
    if query:
        colaboradores = Colaborador.objects.filter(nombre__icontains=query)
    else:
        colaboradores = Colaborador.objects.all()
    return render(request, "myapp/colaboradores.html", {"colaboradores": colaboradores})

def sedes(request):
    query = request.GET.get("q")
    if query:
        sedes = Sede.objects.filter(nombre__icontains=query) |  Sede.objects.filter(direccion__icontains=query)
    else:
        sedes = Sede.objects.all()
    return render(request, "myapp/sedes.html", {"sedes": sedes})



def formulario_componentes_api(request):
    if request.method == "POST":
        componente_form = ComponenteFormulario(request.POST)

        if componente_form.is_valid():
            info_limpia = componente_form.cleaned_data
            componente = Componente(nombre=info_limpia["nombre"], cantidad=info_limpia["cantidad"])
            componente.save()
            return redirect("componentes")
    else:
        componente_form = ComponenteFormulario()

    contexto = {"form": componente_form}

    return render(request, "myapp/forms/componente-formulario.html", contexto)


def formulario_sede_api(request):
    if request.method == "POST":
        sede_form = SedeFormulario(request.POST)

        if sede_form.is_valid():
            info_limpia = sede_form.cleaned_data
            sede = Sede(nombre=info_limpia["nombre"], direccion=info_limpia["direccion"], nro_tel=info_limpia["nro_tel"])
            sede.save()
            return redirect("sedes")
    else:
        sede_form = SedeFormulario()

    contexto = {"form": sede_form}

    return render(request, "myapp/forms/sede-formulario.html", contexto)


def formulario_colaborador_api(request):
    if request.method == "POST":
        colaborador_form = ColaboradorFormulario(request.POST)

        if colaborador_form.is_valid():
            info_limpia = colaborador_form.cleaned_data
            colaborador = Colaborador(nombre=info_limpia["nombre"], apellido=info_limpia["apellido"], email=info_limpia["email"], profesion=info_limpia["profesion"])
            colaborador.save()
            return redirect("colaboradores")
    else:
        colaborador_form = ColaboradorFormulario()

    contexto = {"form": colaborador_form}

    return render(request, "myapp/forms/colaborador-formulario.html", contexto)