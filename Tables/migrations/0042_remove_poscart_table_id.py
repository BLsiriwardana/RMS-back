# Generated by Django 5.0.3 on 2024-04-16 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0041_poscart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poscart',
            name='table_id',
        ),
    ]