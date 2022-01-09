# Generated by Django 3.1.7 on 2022-01-01 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=256)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNo', models.CharField(max_length=256)),
                ('batch', models.PositiveSmallIntegerField()),
                ('major', models.CharField(max_length=256)),
                ('GPA', models.FloatField(default=0.0)),
                ('bio', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('education', models.ManyToManyField(related_name='students', to='main.Education')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeId', models.CharField(max_length=256, unique=True)),
                ('associatedSince', models.DateField()),
                ('department', models.CharField(blank=True, max_length=256)),
                ('designation', models.CharField(max_length=256)),
                ('title', models.PositiveSmallIntegerField(choices=[(1, 'Dr.'), (2, 'Mr.'), (3, 'Mrs.'), (4, 'Ms.')])),
                ('education', models.ManyToManyField(related_name='staffs', to='main.Education')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=256)),
                ('year', models.IntegerField(default=2021)),
                ('vacancy', models.PositiveSmallIntegerField()),
                ('recruited', models.PositiveSmallIntegerField()),
                ('eligibilityGPA', models.FloatField()),
                ('offer', models.PositiveSmallIntegerField(choices=[(1, 'Internship'), (2, 'Placement')])),
                ('criteria', models.ManyToManyField(related_name='companyCriteria', to='main.Skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.CharField(default='Pending', max_length=10)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('domain', models.CharField(max_length=256)),
                ('endDate', models.DateField()),
                ('field', models.CharField(max_length=256)),
                ('startDate', models.DateField()),
                ('title', models.CharField(max_length=256)),
                ('url', models.TextField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('addedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('approvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.staff')),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.institution')),
                ('mentors', models.ManyToManyField(blank=True, related_name='projects', to='main.Staff')),
                ('students', models.ManyToManyField(blank=True, related_name='projects', to='main.Student')),
                ('tags', models.ManyToManyField(blank=True, related_name='projects', to='main.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='institution',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.institution'),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.CharField(default='Pending', max_length=10)),
                ('achievedDate', models.DateField()),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('proof', models.URLField(max_length=1000, null=True)),
                ('technical', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=256)),
                ('category', models.PositiveSmallIntegerField(choices=[(0, 'NA'), (1, 'intra college'), (2, 'inter college'), (3, 'district level'), (4, 'state level'), (5, 'national level'), (6, 'international level')], default=1)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('approvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.staff')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.institution')),
                ('mentors', models.ManyToManyField(blank=True, related_name='achievements', to='main.Staff')),
                ('tags', models.ManyToManyField(blank=True, related_name='achievements', to='main.Tag')),
                ('teamMembers', models.ManyToManyField(blank=True, related_name='achievements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]