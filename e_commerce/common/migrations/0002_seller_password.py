# Generated by Django 4.1.3 on 2022-12-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
