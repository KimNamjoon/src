# Generated by Django 2.2.11 on 2020-11-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_auto_20200420_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.CharField(default='2020-11-19-18.15.01', max_length=100),
        ),
    ]