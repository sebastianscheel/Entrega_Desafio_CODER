from email.headerregistry import Address
from django import forms

class ClienteForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "customer-name",
                "placeholder": "Nombre del cliente",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "customer-name",
                "placeholder": "Apellido del cliente",
                "required": "True",
            }
        ),
    )
    address = forms.CharField(
        label="Domicilio",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "customer-name",
                "placeholder": "Domicilio del cliente",
                "required": "True",
            }
        ),
    )
    phone_namber = forms.IntegerField(
        label="Telefono",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "customer-phone",
                "placeholder": "Telefono del cliente",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "customer-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )
    company = forms.CharField(
        label="Empresa",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "customer-company",
                "placeholder": "Empresa en la que trabaja",
                "required": "True",
            }
        ),
    )