from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("why", views.why, name="why"), 
    path("trainer", views.trainer, name="trainer"),
    path("contact", views.contact, name="contact")
]
