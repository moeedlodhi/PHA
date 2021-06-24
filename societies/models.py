from django.db import models
from django.utils import timezone
from UserManagement.models import Users,user_roles



class zones(models.Model):
    parent_id=models.IntegerField()
    zone=models.CharField(max_length=264)
    shortcode=models.CharField(max_length=264)
    call_center_no=models.CharField(max_length=264)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(zones, self).save(*args, **kwargs)


class society(models.Model):
    zone_id=models.ForeignKey(zones,related_name='ZoneSociety',on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=264)
    logo=models.ImageField(null=True,blank=True)
    smsPrefix=models.CharField(max_length=264,null=True,blank=True)
    letterPrefix = models.CharField(max_length=264, null=True, blank=True)
    description = models.CharField(max_length=264, null=True, blank=True)
    status=models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

        if self.zone_id=='' or self.zone_id==None:
            self.is_deleted=True


        return super(society, self).save(*args, **kwargs)


class user_societies(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.SET_NULL,null=True,blank=True,related_name='UserSocieties')
    user_id=models.ForeignKey(Users,related_name='UserSocieties',on_delete=models.SET_NULL,null=True,blank=True)
    role_id=models.ForeignKey(user_roles,related_name='RoleSocieties',on_delete=models.SET_NULL,null=True,blank=True)
    status=models.IntegerField()
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=True


    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

        if self.society_id=='' or self.society_id==None:
            self.is_deleted=True


        return super(user_societies, self).save(*args, **kwargs)



class society_settings(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.SET_NULL,null=True,blank=True)
    setting_key=models.CharField(max_length=264,null=True,blank=True)
    setting_value=models.FloatField(null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

        if self.society_id=='' or self.society_id==None:
            self.is_deleted=True


        return super(society_settings, self).save(*args, **kwargs)

# Remember to add your foreign keys here
class sms_log(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.SET_NULL,related_name='SocietySMS',null=True,blank=True)
    # letter_id=models.ForeignKey()
    # member_id=models.ForeignKey()
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

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

        if self.society_id=='' or self.society_id==None:
            self.is_deleted=True


        return super(sms_log, self).save(*args, **kwargs)



class report_zone_process(models.Model):
    zone_id=models.ForeignKey(zones,on_delete=models.SET_NULL,null=True,blank=True)
    total_process=models.IntegerField(null=True,blank=True)
    total_pending = models.IntegerField(null=True, blank=True)
    total_cancelled=models.IntegerField(null=True, blank=True)
    total_rejected=models.IntegerField(null=True,blank=True)
    process_types_total=models.CharField(max_length=10000,null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

        if self.zone_id=='' or self.zone_id==None:
            self.is_deleted=True


        return super(report_zone_process, self).save(*args, **kwargs)



class report_user_process(models.Model):
    zone_id=models.ForeignKey(zones,on_delete=models.SET_NULL,null=True,blank=True)
    society_id=models.ForeignKey(society,on_delete=models.SET_NULL,null=True,blank=True)
    user_id=models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,blank=True)
    user_role=models.ForeignKey(user_roles,on_delete=models.SET_NULL,null=True,blank=True)
    total_process = models.IntegerField(null=True, blank=True)
    total_pending = models.IntegerField(null=True, blank=True)
    total_approved = models.IntegerField(null=True, blank=True)
    total_cancelled = models.IntegerField(null=True, blank=True)
    total_rejected = models.IntegerField(null=True, blank=True)
    process_types_total=models.CharField(max_length=264,null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

        if self.society_id=='' or self.society_id==None or self.user_id=='' or self.user_id==None:
            self.is_deleted=True


        return super(report_user_process, self).save(*args, **kwargs)


class report_society_process(models.Model):
    zone_id=models.ForeignKey(zones,on_delete=models.SET_NULL,null=True,blank=True)
    society_id=models.ForeignKey(society,on_delete=models.SET_NULL,null=True,blank=True)
    total_process = models.IntegerField(null=True, blank=True)
    total_pending = models.IntegerField(null=True, blank=True)
    total_approved = models.IntegerField(null=True, blank=True)
    total_cancelled = models.IntegerField(null=True, blank=True)
    total_rejected = models.IntegerField(null=True, blank=True)
    process_types_total=models.CharField(max_length=264,null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()

        if self.zone_id=='' or self.zone_id==None or self.society_id=='' or self.society_id=='None':
            self.is_deleted=True



        return super(report_society_process, self).save(*args, **kwargs)



