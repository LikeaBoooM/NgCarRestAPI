# Generated by Django 3.0.5 on 2020-08-23 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(choices=[(1, 'Worst'), (2, 'Bad'), (3, 'Good'), (4, 'Better'), (5, 'Best')])),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='ngapp.Car')),
            ],
        ),
    ]
