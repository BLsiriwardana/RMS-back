# Generated by Django 5.0.3 on 2024-04-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0051_rename_pos_id_order_emp_id_order_table_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipaddress1',
            name='table_number',
            field=models.CharField(max_length=225, null=True),
        ),
    ]