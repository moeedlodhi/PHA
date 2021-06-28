from django.db import models
from django.utils import timezone
from UserManagement.models import Users,user_roles
from societies.models import society,members,plots

from process.models import process



class installments(models.Model):
    society_id = models.ForeignKey(society, on_delete=models.CASCADE, related_name='installments', null=True, blank=True)
    plot_id=models.ForeignKey(plots, on_delete=models.CASCADE, related_name='plotinstallments', null=True, blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='userID', null=True,
                                blank=True)
    approved_by=models.IntegerField(null=True,blank=True)
    member_id = models.ForeignKey(members, on_delete=models.CASCADE, related_name='MembersInstallments', null=True,
                                  blank=True)
    installment_type=models.CharField(max_length=264,null=True,blank=True)
    installment_no=models.IntegerField(null=True,blank=True)
    installment=models.IntegerField(null=True,blank=True)
    installment_date=models.DateField(null=True,blank=True)
    installment_due_date = models.DateField(null=True, blank=True)
    installment_charges=models.IntegerField(null=True,blank=True)
    late_fee=models.IntegerField(null=True,blank=True)
    late_fee_wave_off=models.IntegerField(null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)
    payment_date=models.DateField(null=True,blank=True)
    comments=models.CharField(max_length=1000,null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "installments"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(installments, self).save(*args, **kwargs)


class fee_structure(models.Model):
    fee_type=models.CharField(max_length=264,null=True,blank=True)
    fee = models.CharField(max_length=264, null=True, blank=True)
    status=models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "fee_structure"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(fee_structure, self).save(*args, **kwargs)

class fee(models.Model):
    item_id=models.IntegerField(null=True,blank=True)
    item=models.CharField(null=True,blank=True,max_length=264)
    fee=models.CharField(null=True,blank=True,max_length=264)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "fee"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(fee, self).save(*args, **kwargs)

class documents(models.Model):
    society_id = models.ForeignKey(society, on_delete=models.CASCADE, related_name='societyDocuments', null=True,
                                   blank=True)
    member_id = models.ForeignKey(members, on_delete=models.CASCADE, related_name='MembersDocuments', null=True,
                                  blank=True)
    process_id=models.ForeignKey(process, on_delete=models.CASCADE, related_name='processDocuments', null=True,
                                  blank=True)
    model=models.CharField(max_length=264,null=True,blank=True)
    temp_id=models.CharField(max_length=1000,null=True,blank=True)
    savedTo=models.ImageField(null=True,blank=True)
    document_type=models.CharField(max_length=264,null=True,blank=True)
    file_name=models.CharField(max_length=10000,null=True,blank=True)
    file_size=models.IntegerField(null=True,blank=True)
    file_stype=models.CharField(null=True,blank=True,max_length=264)
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "documents"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(documents, self).save(*args, **kwargs)







# Create your models here.
