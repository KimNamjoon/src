# Generated by Django 2.2.11 on 2020-03-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0012_auto_20200331_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.CharField(default='2020-03-31-14.21.49', max_length=100),
        ),
    ]
