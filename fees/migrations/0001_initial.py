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
            name='fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(blank=True, null=True)),
                ('item', models.CharField(blank=True, max_length=264, null=True)),
                ('fee', models.CharField(blank=True, max_length=264, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'fee',
            },
        ),
        migrations.CreateModel(
            name='fee_structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_type', models.CharField(blank=True, max_length=264, null=True)),
                ('fee', models.CharField(blank=True, max_length=264, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'fee_structure',
            },
        ),
        migrations.CreateModel(
            name='installments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mysql_id', models.IntegerField(blank=True, null=True)),
                ('approved_by', models.IntegerField(blank=True, null=True)),
                ('installment_type', models.CharField(blank=True, max_length=264, null=True)),
                ('installment_no', models.IntegerField(blank=True, null=True)),
                ('installment', models.IntegerField(blank=True, null=True)),
                ('installment_date', models.DateField(blank=True, null=True)),
                ('installment_due_date', models.DateField(blank=True, null=True)),
                ('installment_charges', models.IntegerField(blank=True, null=True)),
                ('late_fee', models.IntegerField(blank=True, null=True)),
                ('late_fee_wave_off', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MembersInstallments', to='societies.members')),
                ('plot_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plotinstallments', to='societies.plots')),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='installments', to='societies.society')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userID', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'installments',
            },
        ),
        migrations.CreateModel(
            name='documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mysql_id', models.IntegerField(blank=True, null=True)),
                ('model', models.CharField(blank=True, max_length=264, null=True)),
                ('temp_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('savedTo', models.ImageField(blank=True, null=True, upload_to='')),
                ('document_type', models.CharField(blank=True, max_length=264, null=True)),
                ('file_name', models.CharField(blank=True, max_length=10000, null=True)),
                ('file_size', models.IntegerField(blank=True, null=True)),
                ('file_type', models.CharField(blank=True, max_length=264, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MembersDocuments', to='societies.members')),
                ('process_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processDocuments', to='process.process')),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='societyDocuments', to='societies.society')),
            ],
            options={
                'db_table': 'documents',
            },
        ),
    ]
