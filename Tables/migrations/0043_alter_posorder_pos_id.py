# Generated by Django 5.0.3 on 2024-04-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0042_remove_poscart_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posorder',
            name='POS_id',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
