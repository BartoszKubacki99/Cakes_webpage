# Generated by Django 4.1.1 on 2022-09-14 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cakes', '0002_remove_product_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='Cakes.category'),
        ),
    ]
