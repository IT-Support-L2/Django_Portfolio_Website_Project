from django.urls import path
from . import views

app_name = "certificates"
urlpatterns = [
    path("information.technology", views.it_certif, name="it_certif"),
    path("digital.marketing", views.dmarketing_certif, name="dmarketing_certif"),
    path("web.development", views.webdev_certif, name="webdev_certif"),

]