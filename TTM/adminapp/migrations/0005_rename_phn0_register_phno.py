# Generated by Django 5.0 on 2024-02-08 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_register_email_alter_register_phn0'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='phn0',
            new_name='phno',
        ),
    ]
