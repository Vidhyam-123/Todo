# Generated by Django 5.2.1 on 2025-07-23 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile/'),
        ),
    ]
