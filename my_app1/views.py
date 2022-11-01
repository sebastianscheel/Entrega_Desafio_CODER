from django.shortcuts import render
from django.contrib import messages

from my_app1.models import Cliente
from my_app1.forms import ClienteForm


def create_client (request):
    if request.method == "POST":
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            data = cliente_form.cleaned_data
            actual_objects = Cliente.objects.filter(
                name=data["name"],
                last_name=data["last_name"],
                address=data["address"],
                phone_namber=data["phone_namber"],
                email=data["email"],
                company=data["company"]        
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El cliente {data['name']} - {data['last_name']} ya está creado",
                )
            else:
                cliente = Cliente(
                    name=data["name"],
                    last_name=data["last_name"],
                    address=data["address"],
                    phone_namber=data["phone_namber"],
                    email=data["email"],
                    company=data["company"],
                )
                cliente.save()
                messages.success(
                    request,
                    f"El cliente {data['name']} - {data['last_name']} creado exitosamente!",
                )
                
            return render(
                request=request,
                context={"clientes": Cliente.objects.all()},
                template_name="my_app1/cliente_list.html",
            )

    cliente_form = ClienteForm(request.POST)
    context_dict = {"form": cliente_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app1/cliente_form.html",
    )
    
def clientes(request):
    return render(
        request=request,
        context={"clientes": Cliente.objects.all()},
        template_name="my_app1/cliente_list.html",
    )
