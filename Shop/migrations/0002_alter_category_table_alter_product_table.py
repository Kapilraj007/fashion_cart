# Generated by Django 4.2.4 on 2023-09-02 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='datas',
        ),
        migrations.AlterModelTable(
            name='product',
            table='datases',
        ),
    ]