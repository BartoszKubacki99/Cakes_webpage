# Generated by Django 4.1.1 on 2022-09-19 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cakes', '0015_alter_order_phone_remove_product_ingredients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cakes.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='numer telefonu:'),
        ),
    ]