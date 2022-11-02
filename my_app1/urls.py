from django.urls import path

from my_app1 import views

app_name = "my_app1"

urlpatterns = [
    path("clientes/",view=views.clientes, name="cliente_list"),
    path("clientes/add",view=views.create_client, name="cliente_add"),  
]