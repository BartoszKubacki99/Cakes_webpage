# Generated by Django 4.1.1 on 2022-09-14 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cakes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Cakes.category'),
        ),
    ]
