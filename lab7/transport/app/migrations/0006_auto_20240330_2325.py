# Generated by Django 3.2.25 on 2024-03-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20240330_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='passport',
            field=models.CharField(max_length=10, verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
    ]
