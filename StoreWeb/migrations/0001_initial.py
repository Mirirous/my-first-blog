# Generated by Django 3.0.7 on 2020-07-23 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(max_length=255, verbose_name='Descripcion')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('value', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor')),
                ('product', models.ManyToManyField(to='StoreWeb.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('value', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoreWeb.Product')),
            ],
        ),
    ]
