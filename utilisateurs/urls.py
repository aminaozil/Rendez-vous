from django.urls import path
from .views import test, login_view, register_view, dashboard, accueil


urlpatterns = [
    path("test/",test, name="test" ),
    path("",accueil, name="accueil" ),
    path("login/",login_view, name="login" ),
    path("register/",register_view, name="register" ),
    path("dashboard/",dashboard, name="dashboard" ),

]
