from django.urls import path
from .views import add_patient, list_patient, details_patient, edit_patient

urlpatterns = [
    path("add_patient/", add_patient, name="add_patient"),
    path("list_patient/", list_patient, name="list_patient"),
    path("details_patient/<int:id>/", details_patient, name="details_patient"),
    path("edit_patient/<int:id>/", edit_patient, name="edit_patient"),



]
