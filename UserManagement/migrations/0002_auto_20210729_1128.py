# Generated by Django 3.2.4 on 2021-07-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userroles',
            old_name='userRoleID',
            new_name='mysql_id',
        ),
        migrations.AddField(
            model_name='userroles',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
