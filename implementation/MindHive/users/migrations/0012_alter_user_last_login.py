# Generated by Django 3.2.12 on 2022-03-12 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 13, 0, 54, 21, 537529)),
        ),
    ]
