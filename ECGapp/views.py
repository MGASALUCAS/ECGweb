from django.shortcuts import render
from ECGapp import app
import importlib


# Create your views here.
def home(request):
    return render(request, 'home.html')


def upload(request):
    importlib.reload(app)
    if True:
        return render(request, 'upload1.html')


def download(request):
    importlib.reload(app)
    if True:
        return render(request, 'download1.html')


def output(request):
    return render(request, 'output.html')
