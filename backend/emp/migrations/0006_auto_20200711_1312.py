# Generated by Django 3.0.7 on 2020-07-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0005_auto_20200711_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='Duration',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
