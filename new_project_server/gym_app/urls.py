from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("why", views.why, name="why"), 
    path("subscription", views.subscription, name="subscription"), 
    path("payment", views.payment, name="payment"),
    path("trainer", views.trainer, name="trainer"),
    path("contact", views.contact, name="contact")
]
