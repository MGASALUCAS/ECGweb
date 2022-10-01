from django.shortcuts import render, redirect
from ECGapp import app
import importlib
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import Patients, Post
from ECGapp import modelHandling1


# Create your views here.
@login_required(login_url='login')
def home(request):
    # form = HomeForm()
    posts = Patients.objects.all()
    args = {'posts': posts}
    return render(request, 'patient_list.html', args)


def upload(request):
    importlib.reload(app)
    if True:
        return render(request, 'upload1.html')


from flask import send_file, redirect, request, render_template
from werkzeug.utils import secure_filename


def download(request):
    filename = 'output.csv'
    return send_file(secure_filename(filename))


def predict(request, TestFiles):
    TestFile = Patients.objects.get(TestFiles=TestFiles)
    TestFile.save()
    if request.method == 'POST':
        f = request.TestFile['TestFile']
        f.save(secure_filename(f.filename))
        _, all_data = modelHandling1.give_prediction(f.filename, 'ECGmodel.h5')

    return redirect('download1.html',allData=all_data)


def uploading(request):
    # if request.method == 'POST':
    #     f = request.files['file']
    #     f.save(secure_filename(f.filename))
    #     # output, pictures_name = modelHandling.give_prediction(f.filename, 'ECGmodel.h5')
    #     # print(pictures_name)
    #     _, all_data = modelHandling1.give_prediction(f.filename, 'ECGmodel.h5')
    #
    #     # return render_template('/download.html',results=pictures_name,tables=[output.to_html(classes='data')], titles=output.columns.values)
    #     return render_template('download1.html', allData=all_data)
    return render(request, 'upload1.html')

def output(request):
    return render(request, 'output.html')


def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {'forms': forms}
    return render(request, 'login.html', context)


def admin_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def add_patient(request):
    forms = PatientForm()
    if request.method == 'POST':
        forms = PatientForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('add-patient')
    patient = Patients.objects.all()
    context = {'forms': forms, 'patient': patient}
    return render(request, 'patient_list.html', context)


from django.views.generic import (
    ListView,
)
from .models import patient


class ListListView(ListView):
    model = patient
    template_name = "list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["list"] = patient.objects.get(id=self.kwargs["list_id"])
        return context
