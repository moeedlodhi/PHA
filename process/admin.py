from django.contrib import admin
from process.models import process_types,process_types_meta,process
admin.site.register(process_types)
admin.site.register(process_types_meta)
admin.site.register(process)

# Register your models here.
