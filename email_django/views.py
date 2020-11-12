from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from email_django.tasks import sleep_until


def index(request):
    return HttpResponse("Django is Working!")


def render_taskbar(request):
    return render(request, "taskbar.html")


def email_send(request):
    sleep_until.delay(15)
    return HttpResponse("<h1>Email sent through Django Client!<h1>")