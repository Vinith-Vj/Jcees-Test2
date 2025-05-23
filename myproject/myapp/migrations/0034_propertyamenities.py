# Generated by Django 5.1 on 2025-05-02 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_propertygallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amentity', models.CharField(max_length=350)),
                ('amentity_image', models.ImageField(upload_to='property/')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenity', to='myapp.property')),
            ],
        ),
    ]
