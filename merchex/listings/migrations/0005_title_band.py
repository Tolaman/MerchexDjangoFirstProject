# Generated by Django 5.0.4 on 2024-05-31 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_title_description_title_sold_title_types_title_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]