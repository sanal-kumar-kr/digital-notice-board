from django.urls import path
from . import views

urlpatterns = [
    path('student_add_work',views.add_work_student),
    path('view_student_work',views.view_work_student),
    path('edit_student_work/<int:id>',views.edit_work_student),
    path('delete_student_work/<int:id>',views.delete_work_student),
    path('update_statuses/<int:id>',views.Status_updates),
    path('edit_status/<int:id>',views.Status_edit),
    path('delete_status/<int:id>',views.delete_status),
    path('update_status_views',views.Status_update_views),
]


