import os
from django import forms
from teloenvio.models import Productores, Pedidos, Estado_Pedido, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group

class DateInput(forms.DateInput):
    input_type = 'date'
    


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

# Formulario para crear usuarios
class FormularioRegistro(forms.ModelForm):
    username = forms.CharField      (label='Nombre de usuario', required=True,
                                        max_length=30, min_length=5,
                                        error_messages={
                                            'required': 'El nombre de usuario es obligatorio',
                                            'max_length': 'El usuario no puede superar los 30 caracteres',
                                            'min_length': 'El usuario debe tener al menos 5 caracteres'
                                        },
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'Ingrese su nombre de usuario',
                                            'class': 'form-control'
                                        })
                                    )
    first_name = forms.CharField    (label='Primer nombre', required = True,
                                        max_length=30,
                                        error_messages={
                                            'required': 'El primer nombre es obligatorio',
                                            'max_length': 'El primer nombre debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese su primer nombre',
                                            'class':'form-control'}),
                                    )
    last_name = forms.CharField     (label='Primer apellido', required = True,
                                        max_length=30,
                                        error_messages={
                                            'required': 'El primer apellido del usuario es obligatorio',
                                            'max_length': 'El primer apellido debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese su primer apellido',
                                            'class':'form-control'}),
                                    )
    email = forms.EmailField        (label='Dirección de email', required = True, 
                                        max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el email del usuario',
                                            'max_length': 'La dirección de email tiene más de 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                                'placeholder':'Ingrese su correo electrónico',
                                                'class':'form-control',
                                                'type':'email'})
                                    )
    rut = forms.CharField           (label='RUT', required = True,
                                    max_length=12,
                                        error_messages={
                                            'required': 'El RUN del usuario es obligatorio',
                                            'max_length': 'El RUN no debe sobrepasar los 12 carácteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese su RUN',
                                            'class':'form-control'}),
                                    )
    id_productor = forms.ModelChoiceField(label='Empresa', empty_label=('Seleccione un emprendedor'),
                                        queryset=Productores.objects.all(), required=False, 
                                        widget= forms.Select(attrs={
                                            'class':'form-select'}),)
    group = forms.ModelChoiceField(
                                    label='Grupo',
                                    queryset=Group.objects.filter(name='Clientes'),
                                    required=True,
                                    widget=forms.Select(attrs={'class': 'form-select'}),
                                )
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name','email', 'rut', 'id_productor', 'group')




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


# Formulario para agregar pedidos
class FormularioPedidos(forms.Form):
    id_productor = forms.ModelChoiceField(label='Emprededor', empty_label=('Seleccione un emprendedor'),
                                        queryset=Productores.objects.all(), required=False, 
                                        widget= forms.Select(attrs={
                                            'class':'form-select'}),)
    nombre_cliente = forms.CharField   (label='Nombre del cliente', required = False,
                                        max_length=60,
                                        error_messages={
                                            'max_length': 'El nombre debe tener como maximo 40 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre del cliente',
                                            'class':'form-control'}),
                                        )
    fecha_entrega = forms.DateField    (label='Fecha de entrega', required=True, 
                                        widget=DateInput(attrs={'class': 'form-control'}))
    direccion_cliente = forms.CharField(label='Dirección del cliente', required = False,
                                        max_length=50,
                                        error_messages={
                                            'max_length': 'La dirección debe tener como maximo 50 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese la dirección del cliente',
                                            'class':'form-control'}),
                                        )
    comuna_cliente = forms.CharField(label='Comuna del cliente', required = False,
                                        max_length=30,
                                        error_messages={
                                            'max_length': 'La comuna debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese la comuna del cliente',
                                            'class':'form-control'}),
                                        )
    telefono_cliente = forms.CharField(label='Teléfono del cliente', required = False,
                                        max_length=12,
                                        error_messages={
                                            'max_length': 'El valor debe tener como máximo 12 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el teléfono del cliente',
                                            'class':'form-control'}),
                                        )
    cantidad_cajas = forms.CharField(label='Cantidad de cajas', required = False,
                                        max_length=4,
                                        error_messages={
                                            'max_length': 'El valor debe tener como máximo 4 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese la cantidad de cajas',
                                            'class':'form-control'}),
                                        )
    peso_total = forms.CharField(label='Peso total (kg)', required = False,
                                        max_length=4,
                                        error_messages={
                                            'max_length': 'El valor debe tener como máximo 4 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el peso total del pedido',
                                            'class':'form-control'}),
                                        )
    valor_pedido = forms.CharField(label='Valor del pedido', required = False,
                                        max_length=10,
                                        error_messages={
                                            'max_length': 'El valor debe tener como máximo 10 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el valor del pedido',
                                            'class':'form-control'}),
                                        )
    id_estado = forms.ModelChoiceField(label='Estado', empty_label=('Seleccione un estado de pedido'),
                                        queryset=Estado_Pedido.objects.all(), required=False, 
                                        widget= forms.Select(attrs={
                                            'class':'form-select'}),)
    medio_pago = forms.CharField(label='Medio de pago', required = False,
                                        max_length=20,
                                        error_messages={
                                            'max_length': 'El medio de pago debe tener como máximo 20 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el medio de pago',
                                            'class':'form-control'}),
                                        )
    
    class Meta:
        model = Pedidos
        fields = ['id_productor', 'nombre_cliente', 'direccion_cliente', 'comuna_cliente', 'cantidad_cajas', 'peso_total', 'valor_pedido', 'id_estado', 'medio_pago',]