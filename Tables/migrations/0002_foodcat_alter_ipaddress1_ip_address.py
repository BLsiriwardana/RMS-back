# Generated by Django 5.0.3 on 2024-03-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodcat',
            fields=[
                ('catImage', models.ImageField(upload_to='catimg')),
                ('cat_id', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('catname', models.CharField(max_length=225)),
                ('Description', models.CharField(max_length=225)),
                ('add_date', models.CharField(max_length=225)),
                ('number_items', models.CharField(max_length=225)),
            ],
        ),
        migrations.AlterField(
            model_name='ipaddress1',
            name='ip_address',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]
