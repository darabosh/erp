# Generated by Django 4.1.1 on 2023-09-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_rename_last_updated_facilityinventory_timestamp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='facilityinventory',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
