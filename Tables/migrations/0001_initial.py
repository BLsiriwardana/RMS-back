# Generated by Django 5.0.3 on 2024-03-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPaddress1',
            fields=[
                ('ip_address', models.CharField(max_length=225)),
                ('table_id', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=225, null=True)),
                ('Time', models.CharField(max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('Code_name', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('table_number', models.CharField(max_length=225)),
                ('max_member', models.CharField(max_length=200)),
                ('pass_code', models.CharField(max_length=200, null=True)),
                ('Table_catogary', models.CharField(max_length=200)),
                ('qr_codes', models.ImageField(blank=True, upload_to='qr_codes')),
                ('times', models.IntegerField(max_length=225, null=True)),
            ],
        ),
    ]
