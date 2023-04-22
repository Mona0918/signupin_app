from django.db import models
from django.contrib.auth.models import User

class SignUpModel(User):
    ProfilePic=models.ImageField(upload_to='profilepic/')
    ConfirmPassword=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    utype=models.CharField(max_length=10,null=False)

class UserTypeModel(models.Model):
    type=[('Patient','PATIENT'),('Doctor','DOCTOR')]
    usertype=models.CharField(max_length=20,choices=type, default='Patient')

    def __str__(self):
        return self.usertype