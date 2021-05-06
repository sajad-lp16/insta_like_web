# Generated by Django 3.2 on 2021-05-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='modeified_time',
        ),
        migrations.RemoveField(
            model_name='like',
            name='modeified_time',
        ),
        migrations.AddField(
            model_name='comment',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, verbose_name='modified time'),
        ),
        migrations.AddField(
            model_name='like',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, verbose_name='modified time'),
        ),
    ]
