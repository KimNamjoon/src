# Generated by Django 2.2.11 on 2020-11-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0020_auto_20200420_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.CharField(default='2020-11-19-20.03.47', max_length=100),
        ),
    ]
