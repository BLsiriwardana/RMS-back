# Generated by Django 5.0.3 on 2024-04-16 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0037_waiterassignhistory_asignwaiters_emp_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='POSorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=225)),
                ('POS_id', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=225, null=True)),
                ('phone', models.CharField(max_length=225, null=True)),
                ('waiter', models.CharField(max_length=225, null=True)),
                ('chef', models.CharField(max_length=225, null=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('payment_method', models.CharField(max_length=225, null=True)),
                ('value', models.CharField(max_length=225, null=True)),
                ('pay_status', models.CharField(max_length=225, null=True)),
                ('action_status', models.CharField(max_length=225, null=True)),
            ],
        ),
    ]
