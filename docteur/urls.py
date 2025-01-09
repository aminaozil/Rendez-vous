from django.urls import path
from .views import add_docteur, details_docteur, edit_docteur, list_docteur, delete_docteur, info_docteur

urlpatterns = [
    path("add/", add_docteur, name="add_docteur"),
    path("list/", list_docteur, name="list_docteur"),
    path("info/", info_docteur, name="info_docteur"),
    path("details/<int:id>/", details_docteur, name="details_docteur"),
    path("edit/<int:id>/", edit_docteur, name="edit_docteur"),
    path("delete/<int:id>/", delete_docteur, name="delete_docteur"),
]
