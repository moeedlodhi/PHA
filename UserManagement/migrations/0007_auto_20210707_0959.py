# Generated by Django 3.2.4 on 2021-07-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0006_auto_20210625_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user_roles',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='user_roles',
            table='user_roles',
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]