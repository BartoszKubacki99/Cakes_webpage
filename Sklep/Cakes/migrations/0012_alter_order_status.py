# Generated by Django 4.1.1 on 2022-09-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cakes', '0011_order_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'zatwierdzony'), (2, 'niezatwierdzony')], default='w trakcie przetwarzania', null=True),
        ),
    ]
