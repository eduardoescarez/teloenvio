# Generated by Django 4.2.3 on 2023-07-11 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teloenvio', '0003_pedidos_fecha_entrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='estado_pedido',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
