# Generated by Django 3.2.4 on 2021-07-29 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20210729_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hikemodel',
            name='hike_description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]