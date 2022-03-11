# Generated by Django 4.0.3 on 2022-03-09 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='content',
            name='dislikedBy',
            field=models.ManyToManyField(related_name='dislikedBy', to='users.user'),
        ),
        migrations.AddField(
            model_name='content',
            name='likedBy',
            field=models.ManyToManyField(related_name='likedBy', to='users.user'),
        ),
    ]
