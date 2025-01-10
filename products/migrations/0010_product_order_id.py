# Generated by Django 5.0.6 on 2024-10-27 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_prod', to='products.orders'),
        ),
    ]
