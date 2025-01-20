from django.urls import path
from . import views

urlpatterns = [
    path('notification_admin_add',views.add_admin_notification),
    path('notification_admin_view',views.view_admin_notification),
    path('edit_notification/<int:id>',views.edit_notification),
    path('edit_staffnotification/<int:id>',views.edit_staffnotification),
    path('delete_notification/<int:id>',views.delete_notification),
    path('delete_staffnotification/<int:id>',views.delete_staffnotification),
    path('notification_staff_add',views.add_staff_notification),
    # path('notification_admin_add_staff',views.add_admin_staff_notification),
    # path('notification_admin_add_student',views.add_admin_student_notification),
]