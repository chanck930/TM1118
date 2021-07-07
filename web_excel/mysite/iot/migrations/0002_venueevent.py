# Generated by Django 3.2.5 on 2021-07-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('timeStart', models.TimeField()),
                ('timeEnd', models.TimeField()),
                ('event', models.CharField(max_length=10)),
                ('instructor', models.CharField(max_length=50)),
            ],
        ),
    ]