# Generated by Django 3.1.7 on 2022-01-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_achievement_proof'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('link', models.TextField(null=True)),
                ('image', models.FileField(upload_to='')),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
