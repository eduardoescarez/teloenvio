# Generated by Django 4.2.3 on 2023-07-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teloenvio', '0002_clientes_productores_productos_pedidos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='fecha_entrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
