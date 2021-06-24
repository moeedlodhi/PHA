from django.contrib import admin
from societies.models import zones,society,user_societies,society_settings,sms_log
admin.site.register(zones)
admin.site.register(society)
admin.site.register(user_societies)
admin.site.register(society_settings)
admin.site.register(sms_log)

# Register your models here.
