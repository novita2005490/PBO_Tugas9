# Generated by Django 3.2.9 on 2021-11-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(),
        ),
    ]
