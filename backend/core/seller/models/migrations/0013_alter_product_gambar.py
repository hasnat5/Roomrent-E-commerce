# Generated by Django 4.1.1 on 2022-12-23 09:27

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0012_alter_product_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gambar',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='static/img/'), upload_to='../../static/img/'),
        ),
    ]
