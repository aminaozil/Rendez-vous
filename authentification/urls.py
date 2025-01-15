

from .views import accueil, login_page, logout_user, info_user, details_user
from django.urls import path
from django.contrib.auth import views


urlpatterns = [
    path("", accueil, name="accueil"),
    path("login/", login_page, name="login"),
    path('logout/', logout_user, name='logout'),
    path("info_user/", info_user, name="info_user"),
    path("details_user/", details_user, name="details_user"),


    path("reset_password/", views.PasswordResetView.as_view(template_name='authentification/password_reset.html'), name="reset_password"),
    path("reset_password_sent/", views.PasswordResetDoneView.as_view(template_name='authentification/password_reset_sent.html'), name="password_reset_done"),
    path("reset/<uidb64>/<token>", views.PasswordResetConfirmView.as_view(template_name='authentification/password_reset_form.html'), name="password_reset_confirm"),
    path("reset_password_complete", views.PasswordResetCompleteView.as_view(template_name='authentification/password_reset_done.html'), name="password_reset_complete"),



   

]
