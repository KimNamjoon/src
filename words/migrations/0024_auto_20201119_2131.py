# Generated by Django 2.2.11 on 2020-11-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0023_auto_20201119_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.CharField(default='2020-11-19-21.31.32', max_length=100),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_with_acute',
            field=models.CharField(default='<django.db.models.fields.CharField>', max_length=100),
        ),
    ]
