# Generated by Django 3.2.5 on 2021-07-23 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0008_alter_process_member_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='process_comments',
            name='comments',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
    ]
