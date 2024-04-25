# Generated by Django 5.0.3 on 2024-04-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0055_topfooditem_alter_tables_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topfooditem',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='topfooditem',
            name='price',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='topfooditem',
            name='short_description',
            field=models.TextField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='topfooditem',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
