# Generated by Django 3.1.7 on 2021-05-14 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stsnsapp', '0007_auto_20210511_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquor',
            name='user_liquor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
