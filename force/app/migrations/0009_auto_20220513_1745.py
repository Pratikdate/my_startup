# Generated by Django 3.2.12 on 2022-05-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_enquiry_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_add',
            name='Company_Logo',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='product_add',
            name='Product_Img',
            field=models.ImageField(blank=True, null=True, upload_to='product_img/'),
        ),
    ]
