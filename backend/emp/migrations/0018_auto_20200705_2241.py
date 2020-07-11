# Generated by Django 3.0.7 on 2020-07-05 20:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0017_auto_20200705_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='NID',
            field=models.CharField(max_length=14, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='National ID must be entered exactly 14 digits.', regex='^(\\d{14})$')]),
        ),
        migrations.AlterField(
            model_name='family',
            name='Proof',
            field=models.FileField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='family',
            name='Relationship',
            field=models.CharField(choices=[('wife', 'Wife'), ('son', 'Son'), ('daughter', 'Daughter'), ('cousin', 'Cousin'), ('husband', 'Husband'), ('friend', 'friend')], default='wife', max_length=9),
        ),
        migrations.AlterUniqueTogether(
            name='family',
            unique_together={('owner', 'NID')},
        ),
    ]