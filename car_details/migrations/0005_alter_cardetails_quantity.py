# Generated by Django 4.2.7 on 2024-01-01 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_details', '0004_carbrand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
