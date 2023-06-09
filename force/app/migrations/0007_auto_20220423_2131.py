# Generated by Django 3.2.12 on 2022-04-23 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_alter_requirement_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_add',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product_enquiry',
            name='Product_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_enquiry', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product_enquiry',
            name='Sender_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sender_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shiping_enquiry',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
