# Generated by Django 4.2.3 on 2023-07-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teloenvio', '0004_pedidos_estado_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Estado de pedido',
                'verbose_name_plural': 'Estado de pedidos',
            },
        ),
    ]
