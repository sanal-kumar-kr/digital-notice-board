from django.urls import path
from . import views

urlpatterns = [
    path('add_department',views.department_add),
    path('view_department',views.department_view),
    path('edit_department/<int:id>',views.department_edit),
    path('delete_department/<int:id>',views.department_delete),
    path('add_semester',views.semester_add),
    path('view_semester',views.semester_view),
    path('edit_semester/<int:id>',views.semester_edit),
    path('delete_semester/<int:id>',views.semester_delete),
]