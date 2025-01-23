from django.urls import path
from .views import add_patient, list_patient, details_patient, edit_patient, PatientListApiView, PatientRetrieveApiView, PatientUpdateApiView, PatientDeleteApiView, PatientCreateApiView

urlpatterns = [
    path("add_patient/", add_patient, name="add_patient"),
    path("list_patient/", list_patient, name="list_patient"),
    path("details_patient/<int:id>/", details_patient, name="details_patient"),
    path("edit_patient/<int:id>/", edit_patient, name="edit_patient"),


   path("list/", PatientListApiView.as_view(), name="patient-list"),
   path("create/", PatientCreateApiView.as_view(), name="patient-create"),
   path("<int:pk>/details", PatientRetrieveApiView.as_view(), name="patient-details"),
   path("<int:pk>/update", PatientUpdateApiView.as_view(), name="patient-update"),
   path("<int:pk>/delete", PatientDeleteApiView.as_view(), name="patient-delete"),

]
