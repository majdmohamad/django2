# Generated by Django 5.1.1 on 2024-10-01 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_test_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 1, 14, 51, 21, 670341)),
        ),
    ]
