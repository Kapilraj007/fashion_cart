# Generated by Django 4.2.4 on 2023-09-04 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_alter_product_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='categoryname',
        ),
    ]