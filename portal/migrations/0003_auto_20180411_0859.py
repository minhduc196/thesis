# Generated by Django 2.0.4 on 2018-04-11 08:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_report_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]