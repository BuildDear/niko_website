# Generated by Django 4.2.6 on 2023-11-16 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='admin',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.telegramadmin'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcategory'),
        ),
    ]
