# Generated by Django 3.2.8 on 2021-10-11 22:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_usersid_document_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersid',
            name='document_id',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(10000000000)]),
        ),
        migrations.AlterField(
            model_name='usersid',
            name='first_name',
            field=models.CharField(max_length=55, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='usersid',
            name='last_name',
            field=models.CharField(max_length=55, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]