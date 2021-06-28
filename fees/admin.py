from django.contrib import admin
from fees.models import fee,fee_structure,installments,documents

admin.site.register(fee)
admin.site.register(fee_structure)
admin.site.register(installments)
admin.site.register(documents)
# Register your models here.
