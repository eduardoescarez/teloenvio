# Generated by Django 4.2.3 on 2023-07-11 15:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teloenvio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.EmailField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Productores',
            fields=[
                ('id_productor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_contacto', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=12)),
                ('razon_social', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=30)),
                ('rubro', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Productor',
                'verbose_name_plural': 'Productores',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=20)),
                ('descripcion_producto', models.CharField(max_length=100)),
                ('precio_producto', models.IntegerField()),
                ('stock_producto', models.IntegerField()),
                ('id_productor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='teloenvio.productores')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('instrucciones_entrega', models.CharField(blank=True, max_length=100, null=True)),
                ('medio_pago', models.CharField(blank=True, max_length=20, null=True)),
                ('cantidad_cajas', models.IntegerField(blank=True, null=True)),
                ('peso_total', models.IntegerField(blank=True, null=True)),
                ('valor_pedido', models.IntegerField(blank=True, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='teloenvio.clientes')),
                ('id_productor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='teloenvio.productores')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
