# Generated by Django 5.0.4 on 2024-06-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]
