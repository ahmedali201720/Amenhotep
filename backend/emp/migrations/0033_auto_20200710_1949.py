# Generated by Django 3.0.7 on 2020-07-10 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0032_store_floornumber'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ownershipstore',
            unique_together={('owner', 'store')},
        ),
    ]