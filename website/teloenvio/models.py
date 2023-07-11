from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
# from django.contrib.auth import get_user_model

# Create your models here.


# Modelo de productores
class Productores(models.Model):
    id_productor = models.AutoField(primary_key=True)
    nombre_contacto = models.CharField(max_length=60, null=False, blank=False)
    rut = models.CharField(max_length=12, null=False, blank=False)
    razon_social = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    comuna = models.CharField(max_length=30, null=False, blank=False)
    rubro = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.razon_social
    class Meta:
        verbose_name = 'Productor'
        verbose_name_plural = 'Productores'


# Modelo de productos
class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=20, null=False, blank=False)
    descripcion_producto = models.CharField(max_length=100, null=False, blank=False)
    precio_producto = models.IntegerField(null=False, blank=False)
    stock_producto = models.IntegerField(null=False, blank=False)
    id_productor = models.ForeignKey(Productores, on_delete=models.DO_NOTHING, null=True, blank = True)

    def __str__(self):
        return self.nombre_producto
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

# Modelo de clientes
class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    correo = models.EmailField(max_length=40, null=False, blank=False)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    telefono = models.CharField(max_length=12, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    comuna = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

# Modelo de pedidos
class Pedidos(models.Model):                
    fecha_creacion = models.DateTimeField(default=timezone.now)
    # idUsuario = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, null=True, blank=True)
    id_productor = models.ForeignKey(Productores, on_delete=models.DO_NOTHING, null=True, blank=True)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING, null=True, blank=True)
    instrucciones_entrega = models.CharField(max_length=100, null=True, blank=True)
    medio_pago = models.CharField(max_length=20, null=True, blank=True)
    cantidad_cajas = models.IntegerField(null=True, blank=True)
    peso_total = models.IntegerField(null=True, blank=True)
    valor_pedido = models.IntegerField(null=True, blank=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    estado_pedido = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


# Modelo de estados de pedido
class Estado_Pedido(models.Model):          # Modelo de estados de pedidos
    estado = models.CharField(max_length=45, null=False, blank=False)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = 'Estado de pedido'
        verbose_name_plural = "Estado de pedidos"


# Modelo para usuarios personalizados
class CustomUser(AbstractUser):             
    rut = models.CharField(max_length=12, null=False, blank=False)
    
    def __str__(self):
        return str(self.username)
    