from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from authentification.models import User
from patient.models import Patient
from rendezvous.models import RendezVous
from . import forms
from django.contrib import messages
from .serializers import UserSerializer

from rest_framework import generics
from api.mixins import StaffPermissionsMixin


class ListUserApiView(StaffPermissionsMixin,
                      generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class DetailUserApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class CreateUserApiView(StaffPermissionsMixin,
                        generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    
    # permission_classes = [permissions.IsAdminUser]
    def perform_create(self, serializer):
        username = serializer.validated_data.get("username")
        last_name = serializer.validated_data.get("last_name")
        first_name = serializer.validated_data.get("first_name")
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")

        return serializer.save()

class UpdateUserApiView(StaffPermissionsMixin,
                        generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        username = serializer.validated_data.get("username")
        last_name = serializer.validated_data.get("last_name")
        first_name = serializer.validated_data.get("first_name")
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        serializer.save()


class DeleteUserApiView(StaffPermissionsMixin,
                        generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'




    
    





def logout_user(request):
    
    logout(request)
    return redirect('login')

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect("/info_user/")
            else:
                messages.error(request, "Email ou mot de passe incorrect")
    return render(
        request, 'authentification/login.html', context={'form': form, 'message': message})


def accueil(request):
    return render(request, "index/accueil.html")

@login_required
def info_user(request):
    utilisateur = request.user
    
    nbr_rendez = RendezVous.objects.filter(medecin=utilisateur).count()
    nbr_patient = Patient.objects.filter(docteur=utilisateur).count()
    return render(request, "authentification/info.html", {"utilisateur": utilisateur, "nbr_rendez":nbr_rendez, "nbr_patient":nbr_patient})

@login_required
def details_user(request):
    utilisateur = request.user
    return render(request, "authentification/details_user.html", {"utilisateur": utilisateur})
