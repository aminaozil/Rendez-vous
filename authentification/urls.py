

from .views import accueil, login_page, logout_user, info_user, details_user
from django.urls import path


urlpatterns = [
    path("", accueil, name="accueil"),
    path("login/", login_page, name="login"),
    path('logout/', logout_user, name='logout'),
    path("info_user/", info_user, name="info_user"),
    path("details_user/", details_user, name="details_user"),

   

]
