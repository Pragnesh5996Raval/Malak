# Generated by Django 3.2.14 on 2022-08-25 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_auto_20220824_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='android_r_token',
            new_name='receiver_token',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='ios_r_token',
        ),
    ]
