# Generated by Django 5.0.6 on 2024-07-07 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dlApplication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='licensereissue',
            old_name='new_license_expiration_date',
            new_name='license_expiration_date',
        ),
        migrations.RenameField(
            model_name='licensereissue',
            old_name='old_license_number',
            new_name='license_number',
        ),
        migrations.RemoveField(
            model_name='licensereissue',
            name='new_license_number',
        ),
        migrations.RemoveField(
            model_name='licensereissue',
            name='old_license_expiration_date',
        ),
        migrations.RemoveField(
            model_name='licenserenewal',
            name='medical_certificate',
        ),
        migrations.RemoveField(
            model_name='licenserenewal',
            name='vision_test_result',
        ),
    ]