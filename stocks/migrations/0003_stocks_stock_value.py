# Generated by Django 3.0.2 on 2020-01-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20200125_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='stock_value',
            field=models.FloatField(default=0, verbose_name='Valor'),
            preserve_default=False,
        ),
    ]
