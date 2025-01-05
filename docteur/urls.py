from django.urls import path
from .views import add_docteur, details_docteur

urlpatterns = [
    path("add/", add_docteur, name="add_docteur"),
    path("details/", details_docteur, name="details_docteur"),
]
