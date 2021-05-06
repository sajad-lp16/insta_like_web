# Generated by Django 3.2 on 2021-05-06 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20210506_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='caption',
            field=models.TextField(default=None, verbose_name='caption'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='activity.comment'),
        ),
    ]