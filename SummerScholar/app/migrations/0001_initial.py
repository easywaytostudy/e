# Generated by Django 2.2.3 on 2019-07-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SummerCamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=100)),
                ('game_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Summer Camp',
                'db_table': 'summer_camp',
            },
        ),
    ]
