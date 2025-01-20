from django.urls import path
from . import views

urlpatterns = [
    path('classallotment_add',views.add_classallotment),
    path('classallotment_view',views.view_classallotment),
    path('classallotment_delete/<int:id>',views.delete_classallotment),
    path('classallotment_edit/<int:id>',views.edit_classallotment),
    path('allot/<int:id>',views.allot_seats),
    path('seat_arrangement_view',views.view_seat),
]