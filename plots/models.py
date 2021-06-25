from django.db import models
from societies.models import society,zones
from django.utils import timezone
from UserManagement.models import Users,user_roles
# Create your models here.

class plot_size_categories(models.Model):
    category=models.CharField(max_length=264)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.category

class plot_size(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,related_name='societyPlotSize',null=True,blank=True)
    size=models.CharField(max_length=264,null=True,blank=True)
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


    def __str__(self):
        return self.size

class plots(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,related_name='societyPlot',null=True,blank=True)
    plot_size_id=models.ForeignKey(plot_size,on_delete=models.CASCADE,related_name='societyPlotSize',null=True,blank=True)
    plot_size_category_id = models.ForeignKey(plot_size_categories, on_delete=models.CASCADE, related_name='societyPlotSize', null=True,
                                     blank=True)
    plot_number = models.IntegerField(null=True, blank=True)
    street_number = models.IntegerField(null=True, blank=True)
    plot_address = models.CharField(max_length=1000, null=True, blank=True)
    block_no = models.CharField(max_length=1000, null=True, blank=True)
    form_no= models.CharField(max_length=1000, null=True, blank=True)
    vide_no= models.CharField(max_length=1000, null=True, blank=True)
    dated=models.DateTimeField(null=True,blank=True)
    rate_per_marla=models.FloatField(null=True,blank=True)
    interest = models.FloatField(null=True, blank=True)
    enhancement_cost = models.FloatField(null=True, blank=True)
    total_cost = models.FloatField(null=True, blank=True)
    alloted_access_area =models.CharField(max_length=1000, null=True, blank=True)
    excess_area_dimension= models.FloatField(null=True, blank=True)
    excess_area_memo_no = models.FloatField(null=True, blank=True)
    plot_quota=models.CharField(max_length=1000, null=True, blank=True)
    meta_data=models.CharField(max_length=1000, null=True, blank=True)
    is_alloted=models.BooleanField(null=True,blank=True)
    is_possessed=models.BooleanField(null=True,blank=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()



class payments(models.Model):
    zone_id=models.ForeignKey(zones,on_delete=models.CASCADE,null=True,blank=True)
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,null=True,blank=True)
    # member_id
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
    otc_payment_token_expiry=models.FloatField(null=True,blank=True)
    payment_type=models.CharField(max_length=264,null=True,blank=True)
    mode_of_payment=models.CharField(max_length=264,null=True,blank=True)
    status=models.CharField(max_length=1000,null=True,blank=True)
    is_deleted=models.BooleanField(default=False)

    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

gender=(('male','male'),('female','female'))

class nominee(models.Model):
    society_id = models.ForeignKey(society, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    # member_id
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

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()



class nfc(models.Model):
    society_id = models.ForeignKey(society, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    # member_id
    nfc_serial=models.CharField(max_length=264,null=True,blank=True)
    nfc_hex=models.CharField(max_length=264,null=True,blank=True)
    token=models.CharField(max_length=264,null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()








class nfc_log(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,null=True,blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    # member_id
    # nfc_id
    log=models.CharField(max_length=264,null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()










