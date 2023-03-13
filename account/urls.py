from django.urls import path
from .import views

urlpatterns = [
    path("login",views.login_request, name="login"),
    path("register",views.kullanici_request, name="register"),
    path("logout",views.cikis_request, name="logout"),

]
