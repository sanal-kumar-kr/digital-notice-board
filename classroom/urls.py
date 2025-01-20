from django.urls import path
from . import views

urlpatterns = [
    path('classroom_add',views.add_classroom),
    path('classroom_view',views.view_classroom),
    path('classroom_edit/<int:id>',views.edit_classroom),
    path('classroom_delete/<int:id>',views.delete_classroom),
]