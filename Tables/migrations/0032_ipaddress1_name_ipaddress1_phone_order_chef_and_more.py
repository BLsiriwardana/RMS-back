# Generated by Django 5.0.3 on 2024-04-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0031_alter_order_action_status_alter_order_pay_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipaddress1',
            name='name',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='ipaddress1',
            name='phone',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='chef',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='waiter',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
