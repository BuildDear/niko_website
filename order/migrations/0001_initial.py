# Generated by Django 4.2.6 on 2023-11-16 08:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'basket',
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='Lviv', max_length=50)),
                ('region', models.CharField(default='Lviv', max_length=100)),
                ('post_id', models.BigIntegerField(default=123)),
            ],
            options={
                'db_table': 'shipping',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_sell', models.IntegerField()),
                ('basket', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.basket')),
            ],
            options={
                'db_table': 'product_detail',
            },
        ),
    ]
