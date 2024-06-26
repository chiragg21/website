# Generated by Django 5.0.6 on 2024-06-12 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('FabricID', models.AutoField(primary_key=True, serialize=False)),
                ('FabricName', models.CharField(max_length=255)),
                ('FabricType', models.CharField(max_length=255)),
                ('ImageLink', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Fvendor',
            fields=[
                ('VendorID', models.AutoField(primary_key=True, serialize=False)),
                ('VendorName', models.CharField(max_length=255)),
                ('VendorMail', models.CharField(blank=True, max_length=400, null=True)),
                ('Phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('FabricID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.fabric')),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Swatch', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='F_V',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeliveryLeadTime', models.IntegerField()),
                ('MaxQuantity', models.IntegerField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ValidFrom', models.DateField()),
                ('ValidTill', models.DateField()),
                ('FabricID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fabric')),
                ('VendorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fvendor')),
            ],
            options={
                'unique_together': {('FabricID', 'VendorID')},
            },
        ),
        migrations.CreateModel(
            name='Saleprice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ValidFrom', models.DateField()),
                ('ValidTill', models.DateField()),
                ('FabricID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fabric')),
            ],
            options={
                'unique_together': {('FabricID', 'ValidFrom', 'ValidTill')},
            },
        ),
    ]
