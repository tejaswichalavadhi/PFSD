# Generated by Django 5.0 on 2024-02-08 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_rename_phn0_register_phno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='phno',
            new_name='phonenumber',
        ),
    ]