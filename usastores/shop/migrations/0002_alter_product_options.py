# Generated by Django 4.0.5 on 2022-11-11 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
