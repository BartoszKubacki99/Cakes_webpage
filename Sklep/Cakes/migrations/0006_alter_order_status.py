# Generated by Django 4.1.1 on 2022-09-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cakes', '0005_alter_order_status_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(blank=True, choices=[('1', 'yes'), ('2', 'no')], null=True),
        ),
    ]