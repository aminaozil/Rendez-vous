from django.urls import path
from .views import add_rv, list_rv, details_rendez, edit_rv, CreateRendezVousApiView,ListRendezVousApiView, UpdateRendezvousApiView, RetrieveRendezVousApiView, DeleteRendezVousApiView

urlpatterns = [
    path("add_rendezvous/", add_rv ,name="add_rendezvous"),
    path("list_rendezvous/", list_rv ,name="list_rendezvous"),
    path("details_rendezvous/<int:id>/", details_rendez ,name="details_rendezvous"),
    path("edit_rendezvous/<int:id>/", edit_rv ,name="edit_rendezvous"),

    path("create/", CreateRendezVousApiView.as_view(), name="create-rendezvous"),
    path("list/", ListRendezVousApiView.as_view(), name="list-rendezvous"),
    path("<int:pk>/details", RetrieveRendezVousApiView.as_view(), name="details-rendezvous"),
    path("<int:pk>/update", UpdateRendezvousApiView.as_view(), name="update-rendezvous"),
    path("<int:pk>/delete", DeleteRendezVousApiView.as_view(), name="delete-rendezvous"),

    

]
