# Generated by Django 3.1.7 on 2021-05-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stsnsapp', '0003_liquor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquor',
            name='how_many_liquor',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
