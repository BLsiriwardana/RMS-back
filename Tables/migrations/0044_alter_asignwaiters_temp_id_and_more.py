# Generated by Django 5.0.3 on 2024-04-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0043_alter_posorder_pos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignwaiters',
            name='temp_id',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='asignwaiters',
            name='temp_name',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='asignwaiters',
            name='temp_status',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
