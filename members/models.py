from django.db import models
from django.utils import timezone
from UserManagement.models import Users,user_roles
from societies.models import society


class migration(models.Model):
    version=models.CharField(max_length=264,null=True,blank=True)
    apply_time=models.TimeField(null=True,blank=True)
    is_deleted=models.BooleanField(default=False)





# Create your models here.
