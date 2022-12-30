# Generated by Django 4.1.3 on 2022-12-30 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_alter_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основная категория')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товара',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, through='catalog.ProductCategory', to='catalog.category', verbose_name='Категории'),
        ),
    ]
