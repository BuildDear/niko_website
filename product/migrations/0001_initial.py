# Generated by Django 4.2.6 on 2023-11-16 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('photo', models.ImageField(upload_to='products_images')),
                ('isShown', models.BooleanField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'website_product',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_category',
            },
        ),
    ]
