# Generated by Django 5.0.4 on 2024-06-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_title_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
