"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Importa vistas desde mainsite
from mainsite.views import IndexView, IndexEmprendedoresView
from teloenvio.views import LoginView, InternalHomeView, ListadoPedidosView, CreateProductorView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('emprededores', IndexEmprendedoresView.as_view(), name='emprendedores'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('internal/home', login_required(InternalHomeView.as_view()), name='internal'),
    path('internal/listadopedidos', login_required(ListadoPedidosView.as_view()), name='listado_pedidos'),
    path('internal/nuevoemprendedor', login_required(CreateProductorView.as_view()), name='nuevo_emprendedor'),
]
