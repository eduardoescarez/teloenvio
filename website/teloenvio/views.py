import os
import random
import string
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from teloenvio.models import CustomUser, Pedidos, Productores
from teloenvio.forms import FormularioLogin, FormularioProductor, FormularioPedidos, FormularioRegistro
from django.core.mail import send_mail

# Genera contraseñas aleatorias
def generate_random_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(6))
    return password



# Create your views here.

# Login al sistema interno
class LoginView(TemplateView): 
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        formulario = FormularioLogin()
        title = 'Acceso al sitio interno'
        mensajes = request.session.get('mensajes', None)
        request.session.pop('mensajes', None)
        return render(request, self.template_name, {'formulario': formulario, 'title': title, 'mensajes': mensajes,})

    def post(self, request, *args, **kwargs):
        title = 'Acceso al sitio interno'
        form = FormularioLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.objects.filter(email=email).first()
            if user is not None:
                if user.is_active:
                    authenticated_user = authenticate(request, username=user.username, password=password)
                    login(request, authenticated_user)
                    return redirect('internal')
            form.add_error('email', 'Se han ingresado las credenciales equivocadas.')
        return render(request, self.template_name, {'form': form, 'title': title})
    
# Crea usuarios
class NuevoUsuarioView(TemplateView):
    template_name = 'crear_usuario.html'

    def get(self, request, *args, **kwargs):
        context = {
            'formulario': FormularioRegistro(),
            'title': 'Registro de Usuario',
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FormularioRegistro(request.POST, request.FILES)
        title = 'Registro de Usuarios'
        if form.is_valid():
            username = form.cleaned_data['username']
            password = generate_random_password()
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            group = form.cleaned_data['group']
            if group:
                group.user_set.add(user)
            # mensajes = {'enviado': True, 'resultado': 'Has creado un nuevo usuario exitosamente'}
            request.session['mensajes'] = {'enviado': True, 'resultado': 'El usuario ha sido creado, tus datos de identificación se enviarán por email'}
            correo_destino = form.cleaned_data['email']
            mensaje = f'''
                Bienvenido a Te lo envío.
                Gracias por registrarte en nuestro sitio web. A continuación se le adjunta su contraseña de acceso
                contraseña :   {password} 
                Muchas Gracias por su preferencia
            '''
            send_mail(
                '[Te lo envio] - Contraseña',
                mensaje,
                os.environ.get('EMAIL_HOST_USER'),  # Usar el correo configurado en settings.py
                [correo_destino],  # Enviar el correo al destinatario ingresado por el usuario
                fail_silently=False
            )
            # messages.success(request, mensajes['resultado'])  # Almacenar el mensaje de éxito
            
            
            return redirect('login')  # Redirigir al formulario de inicio de sesión
        mensajes = {'enviado': False, 'resultado': form.errors}
        context = {
            'formulario': form,
            'mensajes': mensajes,
            'title': title
        }
        return render(request, self.template_name, context)

# Pagina Interna
class InternalHomeView(TemplateView):
    template_name = 'internal.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Bienvenido a Te Lo Envío',
        }
        return render(request, self.template_name, context)
    
# Listado de pedidos
class ListadoPedidosView(TemplateView):
    template_name = 'listado_pedidos.html'
    
    def get(self, request, *args, **kwargs):
        pedidos = Pedidos.objects.all()
        context = {
            'title': 'Consulta de estado de pedidos',
            'pedidos': pedidos,
        }
        return render(request, self.template_name, context)

# Listado de rutas
class RutaPedidosView(TemplateView):
    template_name = 'listado_pedidos.html'
    
    def get(self, request, *args, **kwargs):
        pedidos = Pedidos.objects.all().order_by('fecha_entrega').order_by('comuna_cliente').order_by('direccion_cliente')
        context = {
            'title': 'Consulta de rutas',
            'pedidos': pedidos,
        }
        return render(request, self.template_name, context)


# Crear productor
class CreateProductorView(TemplateView):
    template_name = 'crear_productor.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Registro de emprededores',
            'formulario': FormularioProductor(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = FormularioProductor(request.POST)
        if form.is_valid():
            registro = Productores(
                razon_social = form.cleaned_data['razon_social'],
                rut = form.cleaned_data['rut'],
                rubro = form.cleaned_data['rubro'],
                nombre_contacto = form.cleaned_data['nombre_contacto'],
                direccion = form.cleaned_data['direccion'],
                comuna = form.cleaned_data['comuna'],
            )
            registro.save()
            request.session['mensajes'] = {'enviado': True, 'resultado': 'Se ha añadido el emprendedor.'}
            return redirect('internal')
        else:
            mensajes = {'enviado': False, 'resultado': form.errors}

        context = {
            'form': form,
            'mensajes': mensajes,
            }
        return render(request, self.template_name, context)


# Crear pedido
class CreatePedidoView(TemplateView):
    template_name = 'crear_pedido.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Registro de pedidos',
            'formulario': FormularioPedidos(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = FormularioPedidos(request.POST)
        if form.is_valid():
            registro = Pedidos(
                nombre_cliente = form.cleaned_data['nombre_cliente'],
                direccion_cliente = form.cleaned_data['direccion_cliente'],
                comuna_cliente = form.cleaned_data['comuna_cliente'],
                cantidad_cajas = form.cleaned_data['cantidad_cajas'],
                fecha_entrega = form.cleaned_data['fecha_entrega'],
                peso_total = form.cleaned_data['peso_total'],
                valor_pedido = form.cleaned_data['valor_pedido'],
                medio_pago = form.cleaned_data['medio_pago'],
                id_productor = form.cleaned_data['id_productor'],
                id_estado = form.cleaned_data['id_estado'],
            )
            registro.save()
            request.session['mensajes'] = {'enviado': True, 'resultado': 'Se ha añadido el pedido.'}
            return redirect('internal')
        else:
            mensajes = {'enviado': False, 'resultado': form.errors}

        context = {
            'form': form,
            'mensajes': mensajes,
            }
        return render(request, self.template_name, context)
