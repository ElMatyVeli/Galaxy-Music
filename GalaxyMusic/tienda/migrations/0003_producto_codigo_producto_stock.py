# Generated by Django 5.0.6 on 2024-06-03 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_remove_producto_destacado_alter_producto_foto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
    ]