# Generated by Django 3.2.5 on 2021-07-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0004_auto_20210723_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='plot_block_no',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='process_data',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
