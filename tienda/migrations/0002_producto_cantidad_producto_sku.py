# Generated by Django 4.2.5 on 2023-09-10 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='sku',
            field=models.IntegerField(default=0),
        ),
    ]
