from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from teloenvio.models import CustomUser, Pedidos, Productores
from teloenvio.forms import FormularioLogin, FormularioProductor

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

# Crear productores
class CreateProductorView(TemplateView):
    template_name = 'crear_productor.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Registro de emprendedores',
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
