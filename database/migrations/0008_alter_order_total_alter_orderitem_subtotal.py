# Generated by Django 4.1 on 2023-09-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_order_total_orderitem_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]