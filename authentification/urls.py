

from .views import aff, login_page, logout_user
from django.urls import path


urlpatterns = [
    path("test", aff, name="test"),
    path("login/", login_page, name="login"),
    path('logout/', logout_user, name='logout'),

]
