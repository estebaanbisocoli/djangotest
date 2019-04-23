from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from testapp.models import People


def index(request):
    return render(request = request, template_name="index.html", context={"people": People.objects.all})
