# Generated by Django 2.2 on 2019-04-23 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20190423_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='photo',
            field=models.FileField(default='', upload_to='uploads/'),
        ),
    ]
