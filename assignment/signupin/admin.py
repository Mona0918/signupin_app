from django.contrib import admin
from .models import SignUpModel,UserTypeModel
# Register your models here.
admin.site.register(SignUpModel)
admin.site.register(UserTypeModel)