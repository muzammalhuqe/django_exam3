# Generated by Django 4.2.7 on 2024-01-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_details', '0003_rename_title_cardetails_name_alter_cardetails_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbrand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
