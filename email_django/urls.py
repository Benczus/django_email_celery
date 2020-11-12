from django.urls import path
from email_django import views

urlpatterns=[
    path("", views.index ),
    path("taskbar/", views.render_taskbar),
    path("email_send/", views.email_send)
]