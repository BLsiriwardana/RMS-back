# Generated by Django 5.0.3 on 2024-03-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0007_alter_asignwaiters_asign_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcat',
            name='number_items',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
