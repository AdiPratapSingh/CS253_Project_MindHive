# Generated by Django 3.2.12 on 2022-03-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('home', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='dislikedBy',
            field=models.ManyToManyField(blank=True, related_name='dislikedBy', to='users.User'),
        ),
        migrations.AlterField(
            model_name='content',
            name='likedBy',
            field=models.ManyToManyField(blank=True, related_name='likedBy', to='users.User'),
        ),
    ]
