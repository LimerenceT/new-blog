# Generated by Django 2.0.1 on 2018-03-05 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180305_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='view',
            new_name='views',
        ),
    ]