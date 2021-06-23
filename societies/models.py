from django.db import models
from django.utils import timezone
from UserManagement.models import Users,user_roles



class zones(models.Model):
    parent_id=models.IntegerField()
    zone=models.CharField(max_length=264)
    shortcode=models.CharField(max_length=264)
    call_center_no=models.CharField(max_length=264)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(zones, self).save(*args, **kwargs)


class society(models.Model):
    zone_id=models.ForeignKey(zones,related_name='ZoneSociety',on_delete=models.CASCADE)
    name=models.CharField(max_length=264)
    logo=models.ImageField(null=True,blank=True)
    smsPrefix=models.CharField(max_length=264,null=True,blank=True)
    letterPrefix = models.CharField(max_length=264, null=True, blank=True)
    description = models.CharField(max_length=264, null=True, blank=True)
    status=models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(society, self).save(*args, **kwargs)


class user_societies(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,related_name='UserSocieties')
    user_id=models.ForeignKey(Users,related_name='UserSocieties',on_delete=models.CASCADE)
    role_id=models.ForeignKey(user_roles,related_name='RoleSocieties',on_delete=models.CASCADE)
    status=models.IntegerField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(user_societies, self).save(*args, **kwargs)



class society_settings(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE)
    setting_key=models.CharField(max_length=264,null=True,blank=True)
    setting_value=models.FloatField(null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(society_settings, self).save(*args, **kwargs)

# Create your models here.
