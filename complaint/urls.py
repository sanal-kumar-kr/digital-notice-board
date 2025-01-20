from django.urls import path
from . import views

urlpatterns = [
    path('add_complaint',views.complaint_add),
    path('view_complaint',views.complaint_views),
    path('delete_complaint/<int:id>',views.complaint_delete),
    path('response_complaint/<int:id>',views.complaint_response),
    path('view_response_complaint',views.complaint_response_view),
]