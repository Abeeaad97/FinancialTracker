# Generated by Django 3.0.3 on 2020-03-10 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200309_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(max_length=10),
        ),
    ]
