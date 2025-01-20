from django.urls import path
from . import views

urlpatterns = [
    path('feedback_add',views.add_feedback),
    path('feedback_view',views.view_feedback),
    path('feedback_response/<int:id>',views.response_feedback),
    
]