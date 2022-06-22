from cmath import log
from django.http import HttpResponse
from django.shortcuts import render
from appComida.models import Perros, Gatos, Snacks
from django.template import loader
from appComida.forms import Form_comida, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def perros(request):
    perros = Perros.objects.all()
    dicc = {"perros" : perros}
    plantilla = loader.get_template("perros.html")
    doc = plantilla.render(dicc)
    return HttpResponse (doc)


def gatos(request):
    gatos = Gatos.objects.all()
    dicc = {"gatos" : gatos}
    plantilla = loader.get_template("gatos.html")
    doc = plantilla.render(dicc)
    return HttpResponse (doc)


def snacks(request):
    snackys = Snacks.objects.all()
    dicc = {"snacks" : snackys}
    plantilla = loader.get_template("snacks.html")
    doc = plantilla.render(dicc)
    return HttpResponse (doc)

@login_required
def comida_perro(request):

    if request.method == "POST":

        mi_form = Form_comida( request.POST )

        if mi_form.is_valid():
            datos = mi_form.cleaned_data

            comida_perro = Perros(nombre=datos['nombre'], desc=datos['desc'], precio=datos['precio'])
            comida_perro.save()
            return render( request, "alta_perro.html")
    
    return render( request, "alta_perro.html")

@login_required
def comida_gato(request):

    if request.method == "POST":

        mi_form = Form_comida( request.POST )

        if mi_form.is_valid():
            datos = mi_form.cleaned_data

            comida_gato = Gatos(nombre=datos['nombre'], desc=datos['desc'], precio=datos['precio'])
            comida_gato.save()
            return render( request, "alta_gato.html")
    
    return render( request, "alta_gato.html")

@login_required
def comida_snacks(request):

    if request.method == "POST":

        mi_form = Form_comida( request.POST )

        if mi_form.is_valid():
            datos = mi_form.cleaned_data

            comida_snacks = Snacks(nombre=datos['nombre'], desc=datos['desc'], precio=datos['precio'])
            comida_snacks.save()
            return render( request, "alta_snacks.html")
    
    return render( request, "alta_snacks.html")


def buscar_comida(request):

    return render ( request, "buscar_comida.html")


def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        alimento = Perros.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html" , {"alimento" : alimento})
    else:
        return HttpResponse("No se encontro ese alimento")


@login_required
def elimina_perros(request, id):

    comida = Perros.objects.get(id=id)
    comida.delete()

    comida = Perros.objects.all()

    return render(request, "perros.html", {"perros":comida})

@login_required
def elimina_gatos(request, id):

    comida = Gatos.objects.get(id=id)
    comida.delete()

    comida = Gatos.objects.all()

    return render(request, "gatos.html", {"gatos":comida})

@login_required
def elimina_snacks(request, id):

    comida = Snacks.objects.get(id=id)
    comida.delete()

    comida = Snacks.objects.all()

    return render(request, "snacks.html", {"snacks":comida})

@login_required
def editarP(request, id):

    comida = Perros.objects.get(id=id)

    if request.method == "POST":

        mi_form = Form_comida(request.POST)

        if mi_form.is_valid():

            datos = mi_form.cleaned_data
            comida.nombre = datos["nombre"]
            comida.desc = datos["desc"]
            comida.precio = datos["precio"]
            comida.save()

            comida = Perros.objects.all()

            return render(request, "perros.html", {"perros":comida})
    else:
        mi_form = Form_comida(initial={'nombre':comida.nombre, 'desc':comida.desc, 'precio':comida.precio})

    return render(request, "editar_perros.html", {"mi_form":mi_form, "comida":comida})

@login_required
def editarG(request, id):

    comida = Gatos.objects.get(id=id)

    if request.method == "POST":

        mi_form = Form_comida(request.POST)

        if mi_form.is_valid():

            datos = mi_form.cleaned_data
            comida.nombre = datos["nombre"]
            comida.desc = datos["desc"]
            comida.precio = datos["precio"]
            comida.save()

            comida = Gatos.objects.all()

            return render(request, "gatos.html", {"gatos":comida})
    else:
        mi_form = Form_comida(initial={'nombre':comida.nombre, 'desc':comida.desc, 'precio':comida.precio})

    return render(request, "editar_gatos.html", {"mi_form":mi_form, "comida":comida})

@login_required
def editarS(request, id):

    comida = Snacks.objects.get(id=id)

    if request.method == "POST":

        mi_form = Form_comida(request.POST)

        if mi_form.is_valid():

            datos = mi_form.cleaned_data
            comida.nombre = datos["nombre"]
            comida.desc = datos["desc"]
            comida.precio = datos["precio"]
            comida.save()

            comida = Snacks.objects.all()

            return render(request, "snacks.html", {"snacks":comida})
    else:
        mi_form = Form_comida(initial={'nombre':comida.nombre, 'desc':comida.desc, 'precio':comida.precio})

    return render(request, "editar_snacks.html", {"mi_form":mi_form, "comida":comida})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                return render(request, "inicio_UsuarioLogueado.html", {"mensaje":f"{username}"})

        else:
            return render(request, "login.html", {"form":form})

    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return render(request, "index.html", {"mensaje":f"Bienvenido/a"})

    else:
        form = UserCreationForm()
    return render(request,"registro.html",{"form":form})


@login_required
def editarPerfil(request):

    username = request.user

    if request.method == "POST":

        mi_form = UserEditForm(request.POST)

        if mi_form.is_valid():

            info = mi_form.cleaned_data

            username.email = info['email']
            password = info['password1']
            username.set_password(password)
            username.save()

            return render(request, "inicio_UsuarioLogueado.html")

    else:

        mi_form = UserEditForm(initial={'email':username.email})

    return render(request, "editar_perfil.html", {"mi_form":mi_form, "username":username})

