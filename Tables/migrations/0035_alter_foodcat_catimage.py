# Generated by Django 5.0.3 on 2024-04-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0034_foodcat_time_alter_foodcat_add_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcat',
            name='catImage',
            field=models.ImageField(null=True, upload_to='catimg'),
        ),
    ]
