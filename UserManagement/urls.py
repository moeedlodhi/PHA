from django.contrib import admin
from django.urls import path, include
from UserManagement import views

# users/

urlpatterns = [
    path("login/", views.login_user),
    path("superuser/",views.superuser),
    path('user_roles/',views.user_roles1),
    path('users/',views.user1),
    path('user_societies/',views.user_societies1),
    path('settings/',views.settings1),
    path('report_user_process/',views.report_user_proccess_pull),
    path('process_types/',views.process_types1),
    path('process_meta/',views.process_types_meta1),
    path('plot_size/',views.plot_size1),
    path('plots/',views.plots1),
    path('members/',views.members1),
    path('member_plots/',views.member_plots1),
    path('member_meta/',views.member_meta1),
    path('member_activity/',views.member_activity1),
    path('payments/',views.payments1),
    path('letters/',views.letters1),
    path('installments/',views.installments1),
    path('contacts/',views.contacts1),
    path('logout/',views.logout)


]