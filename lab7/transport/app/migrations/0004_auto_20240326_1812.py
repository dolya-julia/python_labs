# Generated by Django 3.2.25 on 2024-03-26 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_passenger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='routes',
        ),
        migrations.AddField(
            model_name='route',
            name='passengers',
            field=models.ManyToManyField(to='app.Passenger'),
        ),
    ]
