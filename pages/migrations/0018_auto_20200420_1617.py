# Generated by Django 2.2.11 on 2020-04-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20200417_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.CharField(default='2020-04-20-16.17.18', max_length=100),
        ),
    ]
