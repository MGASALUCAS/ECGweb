from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Patients(models.Model):
    FullName = models.CharField(max_length=100)
    Patient_id_No = models.IntegerField()
    TestFiles = models.FileField(upload_to='Files/')
    blood_group_choice = (
        ('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),

    )
    blood_group = models.CharField(choices=blood_group_choice, max_length=5)
    date_of_birth = models.DateField()
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    phone_no = models.CharField(max_length=11)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.FullName


class patient(models.Model):
    Name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.Name


class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
