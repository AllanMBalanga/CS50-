from django.urls import path
from . import views

#hello/

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet),
]