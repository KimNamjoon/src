# Generated by Django 2.2.11 on 2020-11-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_merge_20201119_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.CharField(default='2020-11-19-21.27.05', max_length=100),
        ),
    ]