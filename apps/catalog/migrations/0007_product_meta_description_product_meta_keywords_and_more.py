# Generated by Django 4.1.3 on 2023-01-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title'),
        ),
    ]
