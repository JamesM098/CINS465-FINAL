# Generated by Django 3.2.4 on 2021-07-29 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_hikemodel_hike_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hikemodel',
            name='hike_location',
        ),
    ]
