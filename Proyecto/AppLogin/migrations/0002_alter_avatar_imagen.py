# Generated by Django 4.1.4 on 2023-01-28 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(upload_to='Avatars'),
        ),
    ]
