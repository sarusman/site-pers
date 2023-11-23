from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(".well-known/acme-challenge/iOBtt5U4fsQBzb2L5SSsIlkVQ1AQ2G9cyJTcorkwbGY", views.checker, name="index"),
]