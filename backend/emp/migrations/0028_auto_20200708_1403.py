# Generated by Django 3.0.7 on 2020-07-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0027_auto_20200708_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tower',
            name='Papers',
        ),
        migrations.AlterField(
            model_name='tower',
            name='Number',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]