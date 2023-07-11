from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from teloenvio.models import Productos

# Create your views here.


# Indice principal, para personas
class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        title = 'Personas'
        return render(request, self.template_name, {'title': title})
    
# Indice principal, para emprendedores
class IndexEmprendedoresView(TemplateView):
    template_name = 'index_emprendedores.html'

    def get(self, request, *args, **kwargs):
        title = 'Empredendores'
        return render(request, self.template_name, {'title': title})
    
class CatalogoView(TemplateView):
    template_name = 'catalogo.html'

    def get(self, request, *args, **kwargs):
        productos = Productos.objects.all().order_by('id_producto')
        context = {
                'title' : 'Catálogo',
                'productos': productos,
                'cantidad_productos': len(productos),
        }
        return render(request, self.template_name, context)