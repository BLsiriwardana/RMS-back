# Generated by Django 5.0.3 on 2024-03-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0015_alter_cart_quantity_alter_cart_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.IntegerField(),
        ),
    ]
