# Generated by Django 5.1.1 on 2024-09-19 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_orderitem_order_remove_shippingaddress_order_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
