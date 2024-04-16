# Generated by Django 5.0.3 on 2024-04-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0038_posorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posorder',
            name='id',
        ),
        migrations.AddField(
            model_name='posorder',
            name='discount',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='posorder',
            name='order_id',
            field=models.CharField(max_length=225, primary_key=True, serialize=False),
        ),
    ]