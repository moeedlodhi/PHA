from django.contrib import admin
from societies.models import zones,society,user_societies,society_settings,sms_log,report_zone_process,report_user_process, report_society_process,\
    letters,members,member_meta,member_plots,member_activity,\
    member_employee_info,contacts,plots,plot_size,plot_size_categories,payments,nominee,nfc

admin.site.register(zones)
admin.site.register(society)
admin.site.register(user_societies)
admin.site.register(society_settings)
admin.site.register(report_zone_process)
admin.site.register(report_user_process)
admin.site.register(report_society_process)
admin.site.register(letters)
admin.site.register(members)
admin.site.register(member_activity)
admin.site.register(member_meta)
admin.site.register(member_plots)
admin.site.register(member_employee_info)
admin.site.register(contacts)
admin.site.register(plots)
admin.site.register(plot_size)
admin.site.register(plot_size_categories)
admin.site.register(payments)
admin.site.register(nominee)
admin.site.register(nfc)






# Register your models here.
