from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(username=username,)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username,password=password,)
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserRoles(models.Model):
    role = models.CharField(max_length=264, null=True, blank=True)
    mysql_id = models.IntegerField(null=True, blank=True)
    role_short = models.CharField(max_length=264, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "user_roles"

    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(UserRoles, self).save(*args, **kwargs)

    def __str__(self):
        return self.role


CHOICE_GENDER = (('male', 'male'), ('female', 'female'))


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    admin_id = models.IntegerField(default=1)
    role_id = models.ForeignKey(UserRoles, related_name='roles', on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=264, null=True, blank=True)
    first_name = models.CharField(max_length=264, null=True, blank=True)
    middle_name = models.CharField(max_length=264, null=True, blank=True)
    last_name = models.CharField(max_length=264, null=True, blank=True)
    father_name = models.CharField(max_length=264, null=True, blank=True)
    husband_name = models.CharField(max_length=264, null=True, blank=True)
    gender = models.CharField(max_length=264, null=True, blank=True)
    cnic = models.CharField(max_length=264, null=True, blank=True)
    Address = models.CharField(max_length=264, null=True, blank=True)
    city = models.CharField(max_length=1000, null=True, blank=True)
    mobile_number = models.CharField(max_length=264, null=True, blank=True)
    landline_number = models.CharField(max_length=264, null=True, blank=True)
    user_sign = models.ImageField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=2640, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     # if not self.id:
    #     #     self.created_at = timezone.now()
    #     # self.updated_at = timezone.now()
    #
    #     if self.role_id=='' or self.role_id==None:
    #         self.is_deleted=True
    #
    #     return super(Users, self).save(*args, **kwargs)

    USERNAME_FIELD = 'username'

    objects = MyAccountManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser


class settings(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='settingsUsers', null=True, blank=True)
    setting_key = models.CharField(max_length=264, null=True, blank=True)
    setting_value = models.CharField(max_length=264, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "settings"

    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(settings, self).save(*args, **kwargs)
