from django.urls import path
from . import views

urlpatterns = [
    path('exam_add',views.add_exam),
    path('exam_view',views.view_exam),
    path('exam_delete/<int:id>',views.delete_exam),
    path('exam_edit/<int:id>',views.edit_exam),
    path('student_notes',views.student_notes),
  

    
    
]