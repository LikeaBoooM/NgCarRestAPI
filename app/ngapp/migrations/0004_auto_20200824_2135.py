# Generated by Django 3.0.5 on 2020-08-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngapp', '0003_auto_20200823_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='grade',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]),
        ),
    ]
