from django.db import models
from django.utils import timezone
from UserManagement.models import Users
from societies.models import society,members,plots

from process.models import process



class bio_tokens(models.Model):
    society_id=models.ForeignKey(society,on_delete=models.CASCADE,null=True,blank=True,related_name='biotoken')
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='userIDbiotoken', null=True,
                                blank=True)
    process_type=models.CharField(max_length=264,null=True,blank=True)
    token=models.CharField(max_length=1000,null=True,blank=True)
    expiery=models.DateTimeField(null=True,blank=True)
    is_used=models.BooleanField(null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "bio_tokens"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(bio_tokens, self).save(*args, **kwargs)
class bio_lists(models.Model):
    society_id = models.ForeignKey(society, on_delete=models.CASCADE, null=True, blank=True, related_name='biolist')
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='bioListsusers', null=True,
                                blank=True)
    process_id = models.ForeignKey(process, on_delete=models.CASCADE, related_name='processBiotokens', null=True,
                                   blank=True)
    member_id = models.ForeignKey(members, on_delete=models.CASCADE, related_name='MembersBiolists', null=True,
                                  blank=True)
    process_type=models.CharField(max_length=264,null=True,blank=True)
    token=models.CharField(max_length=2000,null=True,blank=True)
    bio_type=models.CharField(max_length=2000,null=True,blank=True)
    source=models.ImageField(null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "bio_lists"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(bio_lists, self).save(*args, **kwargs)


# Create your models here.
