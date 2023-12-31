# Generated by Django 3.2.7 on 2023-01-07 09:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('name', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classproject',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('featured_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinalTT',
            fields=[
                ('zefile', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('name', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exampleproject.branch')),
            ],
        ),
        migrations.CreateModel(
            name='subjecthrs',
            fields=[
                ('subject_hrs', models.CharField(max_length=400)),
                ('priority', models.CharField(default='0', max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=400)),
                ('end_date', models.CharField(max_length=400)),
                ('num_subjects', models.IntegerField(blank=True, default=0, null=True)),
                ('weekday_hrs', models.IntegerField(blank=True, default=0, null=True)),
                ('weekend_hrs', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_date', models.CharField(max_length=400)),
                ('custom_hrs', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('name', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='whatsubjects',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('subjects', models.ManyToManyField(blank=True, to='exampleproject.subject')),
            ],
        ),
        migrations.CreateModel(
            name='unit',
            fields=[
                ('name', models.CharField(max_length=400)),
                ('weightage', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('topic', models.ManyToManyField(blank=True, to='exampleproject.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.ManyToManyField(blank=True, to='exampleproject.unit')),
            ],
        ),
        migrations.CreateModel(
            name='sumn',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('units', models.ManyToManyField(blank=True, to='exampleproject.unit')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='units',
            field=models.ManyToManyField(blank=True, to='exampleproject.unit'),
        ),
        migrations.CreateModel(
            name='semester',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('branches', models.ManyToManyField(blank=True, to='exampleproject.branch')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exampleproject.classproject')),
            ],
        ),
    ]
