# Generated by Django 3.1.7 on 2022-01-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]