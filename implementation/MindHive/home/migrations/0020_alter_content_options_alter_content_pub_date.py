# Generated by Django 4.0.3 on 2022-03-17 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_content_options_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={},
        ),
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 17, 17, 8, 45, 193719), verbose_name='date published'),
        ),
    ]
