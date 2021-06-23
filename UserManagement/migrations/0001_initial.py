# Generated by Django 3.0.5 on 2021-06-22 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=264)),
                ('role_short', models.CharField(max_length=264)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('admin_id', models.IntegerField(default=1)),
                ('first_name', models.CharField(blank=True, max_length=264, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=264, null=True)),
                ('last_name', models.CharField(blank=True, max_length=264, null=True)),
                ('father_name', models.CharField(blank=True, max_length=264, null=True)),
                ('husband_name', models.CharField(blank=True, max_length=264, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=264, null=True)),
                ('cnic', models.CharField(blank=True, max_length=264, null=True)),
                ('Address', models.CharField(blank=True, max_length=264, null=True)),
                ('city', models.CharField(blank=True, max_length=1000, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=264, null=True)),
                ('landline_number', models.CharField(blank=True, max_length=264, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=2640, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='UserManagement.user_roles')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'tbl_users',
            },
        ),
    ]
