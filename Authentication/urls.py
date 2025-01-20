from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('services',views.services),
    path('login',views.doLogin),
    path('logout',views.doLogout),
    path('add_staff',views.add_staff),
    path('view_staff',views.view_staff),
    path('edit_staff/<int:id>',views.edit_staff),
    path('delete_staff/<int:id>',views.delete_staff),
    path('add_student',views.add_student),
    path('view_student',views.view_student),
    path('edit_student/<int:id>',views.edit_student),
    path('delete_student/<int:id>',views.delete_student),
    path('update_profile_staff',views.staff_profile_update),
    path('update_profile_student',views.student_profile_update),
    path('view_profile_staff',views.staff_profile_view),
    path('view_profile_student',views.student_profile_view),
    path('view_profile_admin',views.admin_profile_view),
    path('forgot_password/', views.password_forgot),
    path('admin_reset_password/', views.password_reset),
   
]