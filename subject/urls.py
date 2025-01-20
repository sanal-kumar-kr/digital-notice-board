from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('subject_add',views.add_subject),
    path('add_staff_subject',views.add_staff_subject),
    path('subject_view',views.view_subject),
    path('subject_delete/<int:id>',views.delete_subject),
    path('subject_edit/<int:id>',views.edit_subject),
    path('add_notes/', views.add_notes),
    path('view_notes/', views.view_notes),
    path('delete_notes/<int:id>', views.delete_notes),
    path('edit_notes/<int:id>', views.edit_notes)

   
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)