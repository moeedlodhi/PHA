# Generated by Django 3.2.4 on 2021-07-29 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('societies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bio_tokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_type', models.CharField(blank=True, max_length=264, null=True)),
                ('token', models.CharField(blank=True, max_length=1000, null=True)),
                ('expiery', models.DateTimeField(blank=True, null=True)),
                ('is_used', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biotoken', to='societies.society')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userIDbiotoken', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bio_tokens',
            },
        ),
        migrations.CreateModel(
            name='bio_lists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_type', models.CharField(blank=True, max_length=264, null=True)),
                ('token', models.CharField(blank=True, max_length=2000, null=True)),
                ('bio_type', models.CharField(blank=True, max_length=2000, null=True)),
                ('source', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MembersBiolists', to='societies.members')),
                ('process_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processBiotokens', to='process.process')),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biolist', to='societies.society')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bioListsusers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bio_lists',
            },
        ),
    ]
