# Generated by Django 3.0.5 on 2020-08-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngapp', '0002_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=180, unique=True),
        ),
    ]
