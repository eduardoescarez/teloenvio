from django.contrib import admin
from teloenvio.models import CustomUser, Productores, Productos, Pedidos, Clientes
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomUserAdmin(UserAdmin):                   # Modelo de usuarios personalizados
    model = CustomUser
    list_display = [
        'id',
        'email',
        'username',
        'first_name',
        'last_name',
        'is_staff',
        ]
    ordering = ['id']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('rut',)}),)         # Edición de usuarios en la administración
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('rut',)}),)  # Creación de usuarios en la administración

admin.site.register(CustomUser, CustomUserAdmin)

# Administración de productores
class ProductoresAdmin(admin.ModelAdmin):
    list_display = ['id_productor', 'razon_social', 'rut']
    search_fields = ['razon_social', 'rut']
    ordering = ['id_productor']
    fields  = ['razon_social', 'rut', 'rubro', 'nombre_contacto', 'direccion', 'comuna']

admin.site.register(Productores, ProductoresAdmin)

# Administración de clientes
class ClientesAdmin(admin.ModelAdmin):

    list_display = ['id_cliente', 'nombre']
    search_fields = ['id_cliente', 'nombre']
    ordering = ['id_cliente']
    fields  = [ 'nombre', 'correo', 'telefono', 'direccion', 'comuna']

admin.site.register(Clientes, ClientesAdmin)

# Administración de productos
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['id_producto', 'id_productor','nombre_producto', 'precio_producto', 'stock_producto']
    search_fields = ['nombre_producto', 'precio_producto', 'stock_producto']
    ordering = ['id_producto']
    fields  = [ 'id_productor', 'nombre_producto', 'descripcion_producto', 'precio_producto', 'stock_producto' ]

admin.site.register(Productos, ProductosAdmin)

# Administración de pedidos
class PedidosAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_creacion', 'id_productor', 'id_cliente']
    search_fields = ['id', 'id_productor', 'id_cliente']
    ordering = ['id']
    fields = ['fecha_creacion', 'id_productor', 'id_cliente', 'instrucciones_entrega', 'medio_pago', 'cantidad_cajas', 'peso_total', 'valor_pedido']

admin.site.register(Pedidos, PedidosAdmin)