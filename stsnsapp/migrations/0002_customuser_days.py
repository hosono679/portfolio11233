# Generated by Django 3.1.7 on 2021-05-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stsnsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='days',
            field=models.IntegerField(default=1),
        ),
    ]
