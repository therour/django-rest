# Generated by Django 4.0.3 on 2022-03-20 22:31

import apps.accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geolocation', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('is_member', models.BooleanField(default=False, verbose_name='member status')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', apps.accounts.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20, verbose_name='phone number')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='geolocation.geolocation')),
            ],
        ),
    ]
