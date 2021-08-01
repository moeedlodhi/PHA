from django.urls import path
from UserManagement import views

# users/
urlpatterns = [
    path("login/", views.login_user),
    path('logout/', views.logout_user),
    path('token/', views.is_token_expire),
    path("create_user/", views.create_user),
    path("show_users/", views.show_users),
    path("update_user/", views.update_user),
    path("delete_user/", views.delete_user),

    path("create_user_role/", views.create_user_role),
    path("show_users_roles/", views.show_users_roles),
    path("update_user_role/", views.update_user_role),
    path("delete_user_role/", views.delete_user_role),

    path("superuser/", views.superuser),
    path('user_roles/', views.user_roles1),
    path('users/', views.user1),
    path('user_societies/', views.user_societies1),
    path('settings/', views.settings1),
    path('report_user_process/', views.report_user_proccess_pull),
    path('documents/', views.documents1),
    path('process/', views.process1),
    path('process_types/', views.process_types1),
    path('process_meta/', views.process_types_meta1),
    path('process_comments/', views.process_comments1),
    path('plot_size/', views.plot_size1),
    path('plots/', views.plots1),
    path('members/', views.members1),
    path('member_plots/', views.member_plots1),
    path('member_meta/', views.member_meta1),
    path('member_activity/', views.member_activity1),
    path('payments/', views.payments1),
    path('letters/', views.letters1),
    path('installments/', views.installments1),
    path('contacts/', views.contacts1),
]
