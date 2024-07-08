# Generated by Django 5.0.6 on 2024-07-05 16:57

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('nin', models.CharField(max_length=20, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='NewApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mother_maiden_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('lga', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('nin', models.CharField(max_length=20, unique=True)),
                ('passport_photograph', models.ImageField(upload_to='passport_photos/')),
                ('certificate_number', models.CharField(max_length=20)),
                ('application_type', models.CharField(choices=[('New', 'New'), ('Renewal', 'Renewal'), ('Reissue', 'Reissue')], max_length=10)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Approved', 'Approved'), ('Ready for Printing', 'Ready for Printing')], default='Pending', max_length=20)),
                ('center_location', models.CharField(max_length=100)),
                ('application_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlApplication.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='LicenseRenewal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=20, unique=True)),
                ('license_expiration_date', models.DateField()),
                ('renewal_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vision_test_result', models.BooleanField(default=False)),
                ('medical_certificate', models.FileField(upload_to='medical_certificates/')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlApplication.newapplication')),
            ],
        ),
        migrations.CreateModel(
            name='LicenseReissue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_license_number', models.CharField(max_length=20)),
                ('old_license_expiration_date', models.DateField()),
                ('new_license_number', models.CharField(max_length=20, unique=True)),
                ('new_license_expiration_date', models.DateField()),
                ('reissue_reason', models.TextField()),
                ('reissue_date', models.DateField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlApplication.newapplication')),
            ],
        ),
    ]
