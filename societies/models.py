from django.db import models
from django.utils import timezone
from UserManagement.models import Users, UserRoles




class zones(models.Model):
    parent_id=models.IntegerField()
    zone=models.CharField(max_length=264)
    shortcode=models.CharField(max_length=264)
    call_center_no=models.CharField(max_length=264)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "zones"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(zones, self).save(*args, **kwargs)


class society(models.Model):
    zone_id=models.ForeignKey(zones,related_name='ZoneSociety',on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=264)
    logo=models.ImageField(null=True,blank=True)
    smsPrefix=models.CharField(max_length=264,null=True,blank=True)
    letterPrefix = models.CharField(max_length=264, null=True, blank=True)
    description = models.CharField(max_length=264, null=True, blank=True)
    status=models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    class Meta:
        db_table = "society"


    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()


        return super(society, self).save(*args, **kwargs)


class user_societies(models.Model):
    mysqlid=models.IntegerField(null=True,blank=True)
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,null=True,blank=True,related_name='UserSocieties')
    user_id=models.ForeignKey(Users,related_name='UserSocieties',on_delete=models.CASCADE,null=True,blank=True)
    role_id=models.ForeignKey(UserRoles,related_name='RoleSocieties',on_delete=models.CASCADE,null=True,blank=True)
    status=models.IntegerField()
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    class Meta:
        db_table = "user_societies"


    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()


        return super(user_societies, self).save(*args, **kwargs)



class society_settings(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.SET_NULL,null=True,blank=True)
    setting_key=models.CharField(max_length=264,null=True,blank=True)
    setting_value=models.FloatField(null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)


    class Meta:
        db_table = "society_settings"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at= timezone.now()


        return super(society_settings, self).save(*args, **kwargs)

# Remember to add your foreign keys here




class report_zone_process(models.Model):
    zone_id=models.ForeignKey(zones,on_delete=models.CASCADE,null=True,blank=True)
    total_process=models.IntegerField(null=True,blank=True)
    total_pending = models.IntegerField(null=True, blank=True)
    total_approved = models.IntegerField(null=True, blank=True)
    total_cancelled=models.IntegerField(null=True, blank=True)
    total_rejected=models.IntegerField(null=True,blank=True)
    process_types_total=models.CharField(max_length=10000,null=True,blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    class Meta:
        db_table = "report_zone_process"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()




        return super(report_zone_process, self).save(*args, **kwargs)



class report_user_process(models.Model):
    zone_id=models.ForeignKey(zones,on_delete=models.CASCADE,null=True,blank=True)
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,null=True,blank=True)
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)
    user_role=models.CharField(max_length=264,null=True,blank=True)
    total_process = models.IntegerField(null=True, blank=True)
    total_pending = models.IntegerField(null=True, blank=True)
    total_approved = models.IntegerField(null=True, blank=True)
    total_cancelled = models.IntegerField(null=True, blank=True)
    total_rejected = models.IntegerField(null=True, blank=True)
    process_types_total=models.CharField(max_length=1000000,null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    class Meta:
        db_table = "report_user_process"

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()
    #
    #
    #
    #     return super(report_user_process, self).save(*args, **kwargs)


class report_society_process(models.Model):
    zone_id=models.ForeignKey(zones,on_delete=models.CASCADE,null=True,blank=True)
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,null=True,blank=True)
    total_process = models.IntegerField(null=True, blank=True)
    total_pending = models.IntegerField(null=True, blank=True)
    total_approved = models.IntegerField(null=True, blank=True)
    total_cancelled = models.IntegerField(null=True, blank=True)
    total_rejected = models.IntegerField(null=True, blank=True)
    process_types_total=models.CharField(max_length=10000,null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    class Meta:
        db_table = "report_society_process"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()




        return super(report_society_process, self).save(*args, **kwargs)






class migration(models.Model):
    version=models.CharField(max_length=264,null=True,blank=True)
    apply_time=models.TimeField(null=True,blank=True)
    is_deleted=models.BooleanField(default=False)

CHOICE_GENDER=(('male','male'),
               ('female','female'))


class members(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,related_name='membersSociety',null=True,blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='membersUser', null=True,
                                   blank=True)
    mysql_id=models.IntegerField(null=True,blank=True)
    member_plot_id=models.IntegerField(null=True,blank=True)
    membership_no=models.CharField(max_length=1000,null=True,blank=True)
    society_no = models.CharField(max_length=1000, null=True, blank=True)
    full_name = models.CharField(max_length=1000, null=True, blank=True)
    block= models.CharField(max_length=1000, null=True, blank=True)
    size=models.CharField(max_length=1000,null=True,blank=True)
    type=models.CharField(max_length=264,null=True,blank=True)
    corner=models.IntegerField(null=True,blank=True)
    res_com=models.CharField(max_length=264,null=True,blank=True)
    first_name=models.CharField(max_length=264,null=True,blank=True)
    middle_name = models.CharField(max_length=264, null=True, blank=True)
    last_name = models.CharField(max_length=264, null=True, blank=True)
    fh_type=models.CharField(max_length=264,null=True,blank=True)
    fh_name = models.CharField(max_length=264, null=True, blank=True)
    gender = models.CharField(choices=CHOICE_GENDER,max_length=264, null=True, blank=True)
    cnic=models.CharField(max_length=264,null=True,blank=True)
    current_city = models.CharField(max_length=264, null=True, blank=True)
    profession = models.CharField(max_length=264, null=True, blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    plot_price=models.FloatField(null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)
    allotment_letter=models.IntegerField(null=True,blank=True)
    possession_letter=models.IntegerField(null=True,blank=True)
    digitizing_letter=models.IntegerField(null=True,blank=True)
    is_balloting=models.BooleanField(null=True,blank=True)
    is_auction=models.BooleanField(null=True,blank=True)
    is_open=models.BooleanField(null=True,blank=True)
    is_proxy=models.BooleanField(null=True,blank=True)
    is_imported=models.BooleanField(null=True,blank=True)
    is_exemption=models.BooleanField(null=True,blank=True)
    is_pgshf=models.BooleanField(null=True,blank=True)
    open_date=models.DateTimeField(null=True,blank=True)
    comments=models.TextField(max_length=1000, null=True, blank=True)
    last_activity=models.CharField(max_length=1000,null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)


    class Meta:
        db_table = "members"
    def __str__(self):
        return str(self.mysql_id)

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()
    #
    #
    #     return super(members, self).save(*args, **kwargs)


class letters(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,related_name='letters',null=True,blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='lettersUser', null=True,
                                blank=True)
    member_id = models.ForeignKey(members, on_delete=models.CASCADE, related_name='MembersLetters', null=True,
                                  blank=True)
    mysql_id=models.IntegerField(null=True,blank=True)
    type=models.CharField(max_length=264,null=True,blank=True)
    vars=models.CharField(max_length=264,null=True,blank=True)
    heading=models.CharField(max_length=264,null=True,blank=True)
    body=models.CharField(max_length=264,null=True,blank=True)
    issue_date=models.DateTimeField(null=True,blank=True)
    sms_code=models.CharField(max_length=10000,null=True,blank=True)
    sms_code_hash = models.CharField(max_length=10000, null=True, blank=True)
    president_barcode = models.CharField(max_length=10000, null=True, blank=True)
    president_barcode_hash=models.CharField(max_length=10000, null=True, blank=True)
    gs_barcode=models.CharField(max_length=10000, null=True, blank=True)
    gs_barcode_hash = models.CharField(max_length=10000, null=True, blank=True)
    qr_code = models.CharField(max_length=10000, null=True, blank=True)
    qr_code_hash = models.CharField(max_length=10000, null=True, blank=True)
    rfid_code= models.CharField(max_length=10000, null=True, blank=True)
    rfid_code_hash = models.CharField(max_length=10000, null=True, blank=True)
    is_printed=models.BooleanField(null=True,blank=True)
    print_count=models.IntegerField(null=True,blank=True)
    printing_date=models.DateTimeField(null=True,blank=True)
    printed_by=models.IntegerField(null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "letters"
    #
    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()
    #
    #     return super(letters, self).save(*args, **kwargs)





class member_meta(models.Model):
    member_id = models.ForeignKey(members, on_delete=models.CASCADE, related_name='memberMeta', null=True,
                                  blank=True)
    meta_value=models.CharField(max_length=1000,null=True,blank=True)
    meta_key=models.CharField(max_length=1000,null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "member_meta"

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()
    #
    #     return super(member_meta, self).save(*args, **kwargs)

class member_employee_info(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,related_name='memberemployeeSociety',null=True,
                                 blank=True)
    member_id=models.ForeignKey(members,on_delete=models.CASCADE,related_name='memberEmployee',null=True,
                                 blank=True)
    organization=models.CharField(max_length=264,null=True,blank=True)
    monthly_income=models.IntegerField(null=True,blank=True)
    joining_date=models.DateField(null=True,blank=True)
    service_duration=models.IntegerField(null=True,blank=True
                                    )
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "member_employee_info"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(member_employee_info, self).save(*args, **kwargs)

class member_activity(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='userActivity', null=True,
                                blank=True)
    member_id = models.ForeignKey(members, on_delete=models.CASCADE, related_name='memberActivity', null=True,
                                  blank=True)
    activity=models.CharField(max_length=10000,null=True,blank=True)
    activity_date=models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "member_activity"

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()
    #
    #     return super(member_activity, self).save(*args, **kwargs)


class contacts(models.Model):
    society_id = models.ForeignKey(society, on_delete=models.CASCADE, related_name='contacts', null=True,
                                   blank=True)
    mysql_id=models.IntegerField(null=True,blank=True)
    member_id=models.ForeignKey(members,on_delete=models.CASCADE,null=True,blank=True)
    parent_id=models.IntegerField(null=True,blank=True)
    address_type=models.CharField(max_length=264,null=True,blank=True)
    contact_type = models.CharField(max_length=264, null=True, blank=True)
    contact=models.CharField(max_length=264,null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "contacts"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(contacts, self).save(*args, **kwargs)


class sms_log(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,related_name='SocietySMS',null=True,blank=True)
    letter_id=models.ForeignKey(letters,on_delete=models.CASCADE,null=True,blank=True)
    member_id=models.ForeignKey(members,on_delete=models.CASCADE,null=True,blank=True)
    phone_number=models.CharField(max_length=264,null=True,blank=True)
    sms_code=models.CharField(max_length=264,null=True,blank=True)
    network=models.CharField(max_length=264,null=True,blank=True)
    received_message=models.TextField(max_length=10000,null=True,blank=True)
    response_message = models.TextField(max_length=10000, null=True, blank=True)
    sms_sent=models.BooleanField(null=True,blank=True)
    is_billed=models.BooleanField(null=True,blank=True)
    billed_date=models.DateTimeField(null=True,blank=True)
    is_deleted=models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "sms_log"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at= timezone.now()




        return super(sms_log, self).save(*args, **kwargs)

class plot_size_categories(models.Model):
    category=models.CharField(max_length=264)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "plot_size_categories"

    def __str__(self):
        return self.category

class plot_size(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,related_name='societyPlotSize',null=True,blank=True)
    size_in_units=models.FloatField(null=True,blank=True)
    plot_type=models.CharField(max_length=264,null=True,blank=True)
    rate_per_unit = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    down_payment= models.FloatField(null=True, blank=True)
    installment = models.FloatField(null=True, blank=True)
    installment_period = models.CharField(max_length=264, null=True, blank=True)
    total_installments=models.IntegerField(null=True,blank=True)
    development_charges = models.FloatField(null=True, blank=True)
    transfer_fees = models.FloatField(null=True, blank=True)
    late_installment_surcharges = models.FloatField(null=True, blank=True)
    posession_charge=models.FloatField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    size = models.CharField(max_length=264, null=True, blank=True)
    mysql_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "plot_size"


    def __str__(self):
        return self.size

class plots(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,related_name='societyPlot',null=True,blank=True)
    plot_size_id=models.ForeignKey(plot_size,on_delete=models.CASCADE,related_name='societyPlotSize',null=True,blank=True)
    plot_size_category_id = models.ForeignKey(plot_size_categories, on_delete=models.CASCADE, related_name='societyPlotSize', null=True,
                                     blank=True)
    mysql_id=models.IntegerField(null=True,blank=True)
    plot_number = models.CharField(null=True, blank=True,max_length=264)
    street_number = models.CharField(null=True, blank=True,max_length=264)
    plot_address = models.CharField(max_length=1000, null=True, blank=True)
    block_no = models.CharField(max_length=1000, null=True, blank=True)
    form_no= models.CharField(max_length=1000, null=True, blank=True)
    vide_no= models.CharField(max_length=1000, null=True, blank=True)
    dated=models.DateTimeField(null=True,blank=True)
    rate_per_marla=models.FloatField(null=True,blank=True)
    interest = models.FloatField(null=True, blank=True)
    enhancement_cost = models.FloatField(null=True, blank=True)
    total_cost = models.FloatField(null=True, blank=True)
    alloted_excess_area =models.CharField(max_length=1000, null=True, blank=True)
    excess_area_dimension= models.FloatField(null=True, blank=True)
    excess_area_memo_no = models.FloatField(null=True, blank=True)
    plot_quota=models.CharField(max_length=1000, null=True, blank=True)
    meta_data=models.CharField(max_length=1000, null=True, blank=True)
    is_alloted=models.BooleanField(null=True,blank=True)
    is_possessed=models.BooleanField(null=True,blank=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "plots"

    # def save(self,*args,**kwargs):
    #     if self.excess_area_dimension=='':
    #         self.excess_area_dimension=None
    #     return super(plots, self).save(*args, **kwargs)


class member_plots(models.Model):
    member_id=models.ForeignKey(members,on_delete=models.CASCADE,related_name='Members',null=True,
                                blank=True)
    plot_id=models.ForeignKey(plots,on_delete=models.CASCADE,related_name='Plots',null=True,
                                blank=True)
    mysql_id=models.IntegerField(null=True,blank=True)
    plot_no=models.IntegerField(null=True,blank=True)
    remaining_amount=models.FloatField(null=True,blank=True)
    next_due_date=models.DateField(null=True,blank=True)
    due_date=models.DateField(null=True,blank=True)
    last_payment_date=models.DateField(null=True,blank=True)
    is_active=models.BooleanField(null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "member_plots"

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()
    #
    #     return super(member_plots, self).save(*args, **kwargs)



class payments(models.Model):
    zone_id=models.ForeignKey(zones,on_delete=models.CASCADE,null=True,blank=True)
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,null=True,blank=True)
    member_id=models.ForeignKey(members,on_delete=models.CASCADE,related_name='membersPayments',null=True,
                                blank=True)
    mysql_id=models.IntegerField(null=True,blank=True)
    order_no=models.CharField(max_length=1000, null=True, blank=True)
    plot_no=models.CharField(max_length=256, null=True, blank=True)
    street_number=models.CharField(max_length=1000, null=True, blank=True)
    block_number= models.CharField(max_length=1000, null=True, blank=True)
    plot_address=models.CharField(max_length=1000, null=True, blank=True)
    full_name=models.CharField(max_length=1000, null=True, blank=True)
    cnic=models.CharField(max_length=1000, null=True, blank=True)
    mobile_no=models.CharField(max_length=1000, null=True, blank=True)
    email=models.EmailField(null=True,blank=True)
    amount=models.FloatField(null=True,blank=True)
    fee = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    otc_payment_token=models.CharField(max_length=1000,null=True,blank=True)
    otc_payment_token_expiry=models.CharField(max_length=264,null=True,blank=True)
    payment_type=models.CharField(max_length=264,null=True,blank=True)
    mode_of_payment=models.CharField(max_length=264,null=True,blank=True)
    status=models.CharField(max_length=1000,null=True,blank=True)
    is_deleted=models.BooleanField(default=False)

    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        db_table = "payments"

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()

gender=(('male','male'),('female','female'))

class nominee(models.Model):
    society_id = models.ForeignKey(society, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    member_id=models.ForeignKey(members,on_delete=models.CASCADE,null=True,blank=True,related_name='membersNominee')
    cnic = models.CharField(max_length=1000, null=True, blank=True)
    full_name=models.CharField(max_length=264,null=True,blank=True)
    first_name=models.CharField(max_length=264,null=True,blank=True)
    middle_name = models.CharField(max_length=264, null=True, blank=True)
    last_name = models.CharField(max_length=264, null=True, blank=True)
    relation=models.CharField(max_length=264, null=True, blank=True)
    fh_name=models.CharField(max_length=264, null=True, blank=True)
    gender=models.CharField(choices=gender,max_length=264, null=True, blank=True)
    date_of_birth=models.DateTimeField(null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)
    comments=models.CharField(max_length=264, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "nominee"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()



class nfc(models.Model):
    society_id = models.ForeignKey(society, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    member_id=models.ForeignKey(members,on_delete=models.CASCADE,null=True,blank=True,related_name='membersnfc')
    nfc_serial=models.CharField(max_length=264,null=True,blank=True)
    nfc_hex=models.CharField(max_length=264,null=True,blank=True)
    token=models.CharField(max_length=264,null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "nfc"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()








class nfc_log(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,null=True,blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    member_id=models.ForeignKey(members,on_delete=models.CASCADE,null=True,blank=True,related_name='membersnfclog')
    nfc_id=models.ForeignKey(nfc,on_delete=models.CASCADE,null=True,blank=True,related_name='nfcLog')
    log=models.CharField(max_length=264,null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "nfc_log"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
