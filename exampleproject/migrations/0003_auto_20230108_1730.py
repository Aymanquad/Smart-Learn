# Generated by Django 3.2.7 on 2023-01-08 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exampleproject', '0002_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='branches',
            field=models.ManyToManyField(blank=True, null=True, to='exampleproject.branch'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='curriculum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exampleproject.classproject'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='units',
            field=models.ManyToManyField(blank=True, null=True, to='exampleproject.unit'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
