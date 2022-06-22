from telnetlib import LOGOUT
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('about', views.about, name="about"),
    path('perros', views.perros, name= "perros"),
    path('gatos', views.gatos, name= "gatos"),
    path('snackys', views.snacks, name= "snacks"),
    path('alta_perro', views.comida_perro, name="alta_perro"),
    path('alta_gato', views.comida_gato, name="alta_gato"),
    path('alta_snacks', views.comida_snacks, name="alta_snacks"),
    path("buscar_comida", views.buscar_comida, name="buscar_comida"),
    path("buscar", views.buscar),
    path("elimina_perros/<int:id>", views.elimina_perros, name="elimina_perros"),
    path("elimina_gatos/<int:id>", views.elimina_gatos, name="elimina_gatos"),
    path("elimina_snacks/<int:id>", views.elimina_snacks, name="elimina_snacks"),
    path("editar_perros/<int:id>", views.editarP, name="editar_perros"),
    path("editar_perros", views.editarP, name="editar_perros"),
    path("editar_gatos/<int:id>", views.editarG, name="editar_gatos"),
    path("editar_gatos", views.editarG, name="editar_gatos"),
    path("editar_snacks/<int:id>", views.editarS, name="editar_snacks"),
    path("editar_snacks", views.editarS, name="editar_snacks"),
    path("login", views.login_request, name="Login"),
    path("register", views.register, name="Register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("editarPerfil", views.editarPerfil, name="editarPerfil"),
    
]
