# Generated by Django 3.0.3 on 2020-03-12 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200311_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crypto',
            old_name='name',
            new_name='ticker',
        ),
    ]
