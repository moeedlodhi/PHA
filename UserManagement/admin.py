from django.contrib import admin
from UserManagement.models import Users
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin):


    list_display = ('username', 'email', 'is_admin','is_staff')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('username', 'email','password','gender',"profile_pic")}),

        ('Permissions', {'fields': ('is_admin','is_staff','is_superuser','is_active')}),
    )

    search_fields =  ('username', 'email')
    ordering = ('username','email')

    filter_horizontal = ()


admin.site.register(Users,UserAdmin)

# Register your models here.
