# Generated by Django 3.2.4 on 2021-07-14 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserManagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='letters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=264, null=True)),
                ('vars', models.CharField(blank=True, max_length=264, null=True)),
                ('heading', models.CharField(blank=True, max_length=264, null=True)),
                ('body', models.CharField(blank=True, max_length=264, null=True)),
                ('issue_date', models.DateTimeField(blank=True, null=True)),
                ('sms_code', models.CharField(blank=True, max_length=10000, null=True)),
                ('sms_code_hash', models.CharField(blank=True, max_length=10000, null=True)),
                ('president_barcode_hash', models.CharField(blank=True, max_length=10000, null=True)),
                ('gs_barcode', models.CharField(blank=True, max_length=10000, null=True)),
                ('gs_barcode_hash', models.CharField(blank=True, max_length=10000, null=True)),
                ('qr_barcode', models.CharField(blank=True, max_length=10000, null=True)),
                ('qr_barcode_hash', models.CharField(blank=True, max_length=10000, null=True)),
                ('rfid_code', models.CharField(blank=True, max_length=10000, null=True)),
                ('rfid_code_hash', models.CharField(blank=True, max_length=10000, null=True)),
                ('is_printed', models.BooleanField(blank=True, null=True)),
                ('print_count', models.IntegerField(blank=True, null=True)),
                ('printing_date', models.DateTimeField(blank=True, null=True)),
                ('printed_by', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'letters',
            },
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_plot_id', models.IntegerField(blank=True, null=True)),
                ('membership_no', models.CharField(blank=True, max_length=1000, null=True)),
                ('society_no', models.CharField(blank=True, max_length=1000, null=True)),
                ('full_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('block', models.CharField(blank=True, max_length=1000, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=264, null=True)),
                ('corner', models.IntegerField(blank=True, null=True)),
                ('res_com', models.CharField(blank=True, max_length=264, null=True)),
                ('first_name', models.CharField(blank=True, max_length=264, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=264, null=True)),
                ('last_name', models.CharField(blank=True, max_length=264, null=True)),
                ('fh_type', models.CharField(blank=True, max_length=264, null=True)),
                ('fh_name', models.CharField(blank=True, max_length=264, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=264, null=True)),
                ('cnic', models.CharField(blank=True, max_length=264, null=True)),
                ('current_city', models.CharField(blank=True, max_length=264, null=True)),
                ('profession', models.CharField(blank=True, max_length=264, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('plot_price', models.FloatField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('allotment_letter', models.IntegerField(blank=True, null=True)),
                ('possession_letter', models.IntegerField(blank=True, null=True)),
                ('digitizing_letter', models.IntegerField(blank=True, null=True)),
                ('is_balloting', models.BooleanField(blank=True, null=True)),
                ('is_auction', models.BooleanField(blank=True, null=True)),
                ('is_open', models.BooleanField(blank=True, null=True)),
                ('is_proxy', models.BooleanField(blank=True, null=True)),
                ('is_imported', models.BooleanField(blank=True, null=True)),
                ('is_exemption', models.BooleanField(blank=True, null=True)),
                ('is_pgshf', models.BooleanField(blank=True, null=True)),
                ('open_date', models.DateTimeField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, max_length=1000, null=True)),
                ('last_activity', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='migration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(blank=True, max_length=264, null=True)),
                ('apply_time', models.TimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='nfc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nfc_serial', models.CharField(blank=True, max_length=264, null=True)),
                ('nfc_hex', models.CharField(blank=True, max_length=264, null=True)),
                ('token', models.CharField(blank=True, max_length=264, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membersnfc', to='societies.members')),
            ],
            options={
                'db_table': 'nfc',
            },
        ),
        migrations.CreateModel(
            name='plot_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_in_units', models.FloatField(blank=True, null=True)),
                ('plot_type', models.CharField(blank=True, max_length=264, null=True)),
                ('rate_per_unit', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('down_payment', models.FloatField(blank=True, null=True)),
                ('installment', models.FloatField(blank=True, null=True)),
                ('installment_period', models.CharField(blank=True, max_length=264, null=True)),
                ('total_installments', models.IntegerField(blank=True, null=True)),
                ('development_charges', models.FloatField(blank=True, null=True)),
                ('transfer_fees', models.FloatField(blank=True, null=True)),
                ('late_installment_surcharges', models.FloatField(blank=True, null=True)),
                ('posession_charge', models.FloatField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'plot_size',
            },
        ),
        migrations.CreateModel(
            name='plot_size_categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=264)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'plot_size_categories',
            },
        ),
        migrations.CreateModel(
            name='society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('smsPrefix', models.CharField(blank=True, max_length=264, null=True)),
                ('letterPrefix', models.CharField(blank=True, max_length=264, null=True)),
                ('description', models.CharField(blank=True, max_length=264, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'society',
            },
        ),
        migrations.CreateModel(
            name='zones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField()),
                ('zone', models.CharField(max_length=264)),
                ('shortcode', models.CharField(max_length=264)),
                ('call_center_no', models.CharField(max_length=264)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'zones',
            },
        ),
        migrations.CreateModel(
            name='user_societies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mysqlid', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('role_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RoleSocieties', to='UserManagement.user_roles')),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserSocieties', to='societies.society')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserSocieties', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_societies',
            },
        ),
        migrations.CreateModel(
            name='society_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting_key', models.CharField(blank=True, max_length=264, null=True)),
                ('setting_value', models.FloatField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='societies.society')),
            ],
            options={
                'db_table': 'society_settings',
            },
        ),
        migrations.AddField(
            model_name='society',
            name='zone_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ZoneSociety', to='societies.zones'),
        ),
        migrations.CreateModel(
            name='sms_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=264, null=True)),
                ('sms_code', models.CharField(blank=True, max_length=264, null=True)),
                ('network', models.CharField(blank=True, max_length=264, null=True)),
                ('received_message', models.TextField(blank=True, max_length=10000, null=True)),
                ('response_message', models.TextField(blank=True, max_length=10000, null=True)),
                ('sms_sent', models.BooleanField(blank=True, null=True)),
                ('is_billed', models.BooleanField(blank=True, null=True)),
                ('billed_date', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('letter_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.letters')),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.members')),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SocietySMS', to='societies.society')),
            ],
            options={
                'db_table': 'sms_log',
            },
        ),
        migrations.CreateModel(
            name='report_zone_process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_process', models.IntegerField(blank=True, null=True)),
                ('total_pending', models.IntegerField(blank=True, null=True)),
                ('total_approved', models.IntegerField(blank=True, null=True)),
                ('total_cancelled', models.IntegerField(blank=True, null=True)),
                ('total_rejected', models.IntegerField(blank=True, null=True)),
                ('process_types_total', models.CharField(blank=True, max_length=10000, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('zone_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.zones')),
            ],
            options={
                'db_table': 'report_zone_process',
            },
        ),
        migrations.CreateModel(
            name='report_user_process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role', models.CharField(blank=True, max_length=264, null=True)),
                ('total_process', models.IntegerField(blank=True, null=True)),
                ('total_pending', models.IntegerField(blank=True, null=True)),
                ('total_approved', models.IntegerField(blank=True, null=True)),
                ('total_cancelled', models.IntegerField(blank=True, null=True)),
                ('total_rejected', models.IntegerField(blank=True, null=True)),
                ('process_types_total', models.CharField(blank=True, max_length=1000000, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.society')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zone_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.zones')),
            ],
            options={
                'db_table': 'report_user_process',
            },
        ),
        migrations.CreateModel(
            name='report_society_process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_process', models.IntegerField(blank=True, null=True)),
                ('total_pending', models.IntegerField(blank=True, null=True)),
                ('total_approved', models.IntegerField(blank=True, null=True)),
                ('total_cancelled', models.IntegerField(blank=True, null=True)),
                ('total_rejected', models.IntegerField(blank=True, null=True)),
                ('process_types_total', models.CharField(blank=True, max_length=10000, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.society')),
                ('zone_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.zones')),
            ],
            options={
                'db_table': 'report_society_process',
            },
        ),
        migrations.CreateModel(
            name='plots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_number', models.CharField(blank=True, max_length=264, null=True)),
                ('street_number', models.CharField(blank=True, max_length=264, null=True)),
                ('plot_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('block_no', models.CharField(blank=True, max_length=1000, null=True)),
                ('form_no', models.CharField(blank=True, max_length=1000, null=True)),
                ('vide_no', models.CharField(blank=True, max_length=1000, null=True)),
                ('dated', models.DateTimeField(blank=True, null=True)),
                ('rate_per_marla', models.FloatField(blank=True, null=True)),
                ('interest', models.FloatField(blank=True, null=True)),
                ('enhancement_cost', models.FloatField(blank=True, null=True)),
                ('total_cost', models.FloatField(blank=True, null=True)),
                ('alloted_excess_area', models.CharField(blank=True, max_length=1000, null=True)),
                ('excess_area_dimension', models.FloatField(blank=True, null=True)),
                ('excess_area_memo_no', models.FloatField(blank=True, null=True)),
                ('plot_quota', models.CharField(blank=True, max_length=1000, null=True)),
                ('meta_data', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_alloted', models.BooleanField(blank=True, null=True)),
                ('is_possessed', models.BooleanField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('plot_size_category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='societyPlotSize', to='societies.plot_size_categories')),
                ('plot_size_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='societyPlotSize', to='societies.plot_size')),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='societyPlot', to='societies.society')),
            ],
            options={
                'db_table': 'plots',
            },
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(blank=True, max_length=1000, null=True)),
                ('plot_no', models.CharField(blank=True, max_length=256, null=True)),
                ('street_number', models.CharField(blank=True, max_length=1000, null=True)),
                ('block_number', models.CharField(blank=True, max_length=1000, null=True)),
                ('plot_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('full_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('cnic', models.CharField(blank=True, max_length=1000, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('fee', models.FloatField(blank=True, null=True)),
                ('total_amount', models.FloatField(blank=True, null=True)),
                ('otc_payment_token', models.CharField(blank=True, max_length=1000, null=True)),
                ('otc_payment_token_expiry', models.FloatField(blank=True, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=264, null=True)),
                ('mode_of_payment', models.CharField(blank=True, max_length=264, null=True)),
                ('status', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membersPayments', to='societies.members')),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.society')),
                ('zone_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.zones')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
        migrations.CreateModel(
            name='nominee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnic', models.CharField(blank=True, max_length=1000, null=True)),
                ('full_name', models.CharField(blank=True, max_length=264, null=True)),
                ('first_name', models.CharField(blank=True, max_length=264, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=264, null=True)),
                ('last_name', models.CharField(blank=True, max_length=264, null=True)),
                ('relation', models.CharField(blank=True, max_length=264, null=True)),
                ('fh_name', models.CharField(blank=True, max_length=264, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=264, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=264, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membersNominee', to='societies.members')),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.society')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'nominee',
            },
        ),
        migrations.CreateModel(
            name='nfc_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(blank=True, max_length=264, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membersnfclog', to='societies.members')),
                ('nfc_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nfcLog', to='societies.nfc')),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.society')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'nfc_log',
            },
        ),
        migrations.AddField(
            model_name='nfc',
            name='society_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.society'),
        ),
        migrations.AddField(
            model_name='nfc',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='members',
            name='society_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membersSociety', to='societies.society'),
        ),
        migrations.AddField(
            model_name='members',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membersUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='member_plots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_no', models.IntegerField(blank=True, null=True)),
                ('remaining_amount', models.FloatField(blank=True, null=True)),
                ('next_due_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('last_payment_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Members', to='societies.members')),
                ('plot_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Plots', to='societies.plots')),
            ],
            options={
                'db_table': 'member_plots',
            },
        ),
        migrations.CreateModel(
            name='member_meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_key', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberMeta', to='societies.members')),
            ],
            options={
                'db_table': 'member_meta',
            },
        ),
        migrations.CreateModel(
            name='member_employee_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(blank=True, max_length=264, null=True)),
                ('monthly_income', models.IntegerField(blank=True, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('service_duration', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberEmployee', to='societies.members')),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberemployeeSociety', to='societies.society')),
            ],
            options={
                'db_table': 'member_employee_info',
            },
        ),
        migrations.CreateModel(
            name='member_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(blank=True, max_length=10000, null=True)),
                ('activity_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberActivity', to='societies.members')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userActivity', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'member_activity',
            },
        ),
        migrations.AddField(
            model_name='letters',
            name='member_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MembersLetters', to='societies.members'),
        ),
        migrations.AddField(
            model_name='letters',
            name='society_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='letters', to='societies.society'),
        ),
        migrations.AddField(
            model_name='letters',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lettersUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(blank=True, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('address_type', models.CharField(blank=True, max_length=264, null=True)),
                ('model', models.CharField(blank=True, max_length=264, null=True)),
                ('contact', models.CharField(blank=True, max_length=264, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('society_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='societies.society')),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
    ]
