# Generated by Django 3.1.7 on 2022-01-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
