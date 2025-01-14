from django.urls import path
from .views import add_rv, list_rv, details_rendez

urlpatterns = [
    path("add_rendezvous/", add_rv ,name="add_rendezvous"),
    path("list_rendezvous/", list_rv ,name="list_rendezvous"),
    path("details_rendezvous/<int:id>/", details_rendez ,name="details_rendezvous"),

]
