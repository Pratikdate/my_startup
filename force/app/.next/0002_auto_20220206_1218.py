# Generated by Django 3.2.10 on 2022-02-06 06:48

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager_account',
            name='Slug_Company',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from=['Email', 'Name'], unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manager_account',
            name='Adhar_Number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product_add',
            name='Slug_Product',
            field=autoslug.fields.AutoSlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
