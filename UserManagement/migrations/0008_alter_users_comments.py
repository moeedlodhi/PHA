# Generated by Django 3.2.4 on 2021-08-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0007_alter_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='comments',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
