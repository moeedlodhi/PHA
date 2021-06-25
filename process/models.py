from django.db import models
from django.utils import timezone
from UserManagement.models import Users,user_roles
from societies.models import society
# Create your models here.



class process_types(models.Model):
    type=models.CharField(max_length=264)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(process_types, self).save(*args, **kwargs)

    def __str__(self):
        return self.type

class process_types_meta(models.Model):
    type_id=models.ForeignKey(process_types,related_name='processTypes',on_delete=models.CASCADE,null=True,blank=True)
    meta_key=models.CharField(max_length=264)
    meta_value=models.CharField(max_length=264)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()


        return super(process_types, self).save(*args, **kwargs)

class process(models.Model):
    society_id=models.ForeignKey(society,related_name='societyProcess',on_delete=models.CASCADE,null=True,blank=True)
    user_id=models.ForeignKey(Users,related_name='usersProcess',on_delete=models.CASCADE,null=True,blank=True)
    type_id=models.ForeignKey(process_types,related_name='processtype',on_delete=models.CASCADE,null=True,blank=True)
    assigned_to=models.CharField(null=True,blank=True,max_length=264)
    payment_id=models.CharField(null=True,blank=True,max_length=264)
    member_id=models.CharField(null=True,blank=True,max_length=264)
    plot_id = models.CharField(null=True, blank=True, max_length=264)
    plot_no = models.IntegerField(null=True, blank=True)
    plot_block_no = models.IntegerField(null=True, blank=True)
    plot_address=models.CharField(null=True, blank=True, max_length=264)
    full_name=models.CharField(null=True, blank=True, max_length=264)
    cnic=models.CharField(null=True, blank=True, max_length=264)
    type=models.CharField(null=True, blank=True, max_length=264)
    process_data=models.CharField(null=True, blank=True, max_length=264)
    process_data_back = models.CharField(null=True, blank=True, max_length=264)
    status = models.CharField(null=True, blank=True, max_length=264)
    street_no=models.IntegerField(null=True, blank=True)
    process_no=models.IntegerField(null=True,blank=True)
    is_deleted=models.BooleanField(default=False)

    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()


        return super(process, self).save(*args, **kwargs)



