# Generated by Django 3.2.8 on 2021-10-11 22:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usersid_document_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersid',
            name='document_id',
            field=models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(10000000000)]),
        ),
    ]
