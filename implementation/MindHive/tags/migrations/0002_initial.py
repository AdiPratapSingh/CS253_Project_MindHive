# Generated by Django 4.0.3 on 2022-03-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='users_lst',
            field=models.ManyToManyField(related_name='favourite_of', to='users.user'),
        ),
    ]
