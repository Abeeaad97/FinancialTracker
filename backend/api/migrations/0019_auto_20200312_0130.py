# Generated by Django 3.0.3 on 2020-03-12 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200311_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crypto',
            old_name='ticker',
            new_name='name',
        ),
    ]
