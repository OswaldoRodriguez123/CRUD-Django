# Generated by Django 3.0.2 on 2020-01-25 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='stock_cant',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
    ]