# Generated by Django 4.2.7 on 2024-07-05 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0012_alter_cartorderitem_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorderitem',
            old_name='shipping_amountl',
            new_name='shipping_amount',
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
