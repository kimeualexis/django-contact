# Generated by Django 2.1.7 on 2019-03-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190318_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_male',
            field=models.BooleanField(default=True),
        ),
    ]
