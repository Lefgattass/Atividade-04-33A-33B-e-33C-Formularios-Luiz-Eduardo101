# Generated by Django 3.2.13 on 2023-09-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MCF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=40)),
                ('ano', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('ano', models.DateField()),
                ('potencia', models.IntegerField()),
                ('cv', models.CharField(max_length=3)),
            ],
        ),
    ]