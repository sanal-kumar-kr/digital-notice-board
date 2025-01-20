from django.urls import path
from . import views

urlpatterns = [
    path('add_work',views.Add_Works),
    path('view_work',views.View_Works),
    path('edit_work/<int:id>',views.Edit_work),
    path('delete_work/<int:id>',views.delete_work),
    # path('assign_work/<int:id>',views.assign_works),
    # path('assigned_staff_view/<int:id>',views.assign_staff_view),
    # path('delete_assigned_staff/<int:id>',views.assign_staff_delete),
    # path('view_assign_work',views.Assign_View_Works),
    path('update_status/<int:id>',views.Status_update),
    path('update_status_view',views.Status_update_view),
]