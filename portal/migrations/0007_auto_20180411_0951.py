# Generated by Django 2.0.4 on 2018-04-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20180411_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
