from django.contrib import admin
from process.models import process_types,process_types_meta,process,process_comments
admin.site.register(process_types)
admin.site.register(process_types_meta)
admin.site.register(process)
admin.site.register(process_comments)


# Register your models here.
