import os
from django import forms
from teloenvio.models import Productores

# Formulario de login
class FormularioLogin(forms.Form):
    email = forms.EmailField        (label='Email', required=True,
                                        max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el email del usuario',
                                            'max_length': 'La dirección de email tiene más de 30 caracteres',
                                        },
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'Ingrese su correo electrónico',
                                            'class': 'form-control',
                                            'type': 'email'
                                        })
                                    )
    password = forms.CharField      (label='Contraseña', required=True,
                                        max_length=30, min_length=6,
                                        error_messages={
                                            'required': 'La contraseña es obligatoria',
                                            'max_length': 'La contraseña no puede superar los 30 caracteres',
                                            'min_length': 'La contraseña debe tener al menos 8 caracteres'
                                        },
                                        widget=forms.PasswordInput(attrs={
                                            'placeholder': 'Ingrese su contraseña',
                                            'class': 'form-control'
                                        })
                                    )


# Formulario para agregar productores
class FormularioProductor(forms.Form):
    razon_social = forms.CharField    (label='Nombre del cliente', required = False,
                                        max_length=40,
                                        error_messages={
                                            'max_length': 'El nombre debe tener como maximo 40 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre del productor',
                                            'class':'form-control'}),
                                        )
    rut =          forms.CharField    (label='RUT', required = False,
                                        max_length=12,
                                        error_messages={
                                            'max_length': 'El RUT debe tener como máximo 12 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el RUT del productor',
                                            'class':'form-control'}),
                                        )
    nombre_contacto = forms.CharField   (label='Nombre del contacto', required = False,
                                        max_length=60,
                                        error_messages={
                                            'max_length': 'El nombre debe tener como maximo 60 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre del contacto',
                                            'class':'form-control'}),
                                        )
    rubro = forms.CharField             (label='Rubro', required = False,
                                        max_length=40,
                                        error_messages={
                                            'max_length': 'El rubro debe tener como maximo 40 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el rubro del productor',
                                            'class':'form-control'}),
                                        )
    direccion = forms.CharField        (label='Dirección', required = False,
                                        max_length=50,
                                        error_messages={
                                            'max_length': 'La dirección debe tener como maximo 50 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese la dirección del productor',
                                            'class':'form-control'}),
                                        )
    comuna = forms.CharField           (label='Comuna', required = False,
                                        max_length=30,
                                        error_messages={
                                            'max_length': 'El nombre debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese la comuna',
                                            'class':'form-control'}),
                                        )
    
    class Meta:
        model = Productores
        fields = ['razon_social', 'rut', 'nombre_contacto', 'rubro', 'direccion', 'comuna']


