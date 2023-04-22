from django import forms
from .models import SignUpModel,UserTypeModel
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.ModelForm):
    class Meta:
        model=SignUpModel
        fields=['first_name','last_name','ProfilePic','username','email','password','ConfirmPassword','Address']
        widget={'password':forms.PasswordInput,'ConfirmPassword':forms.PasswordInput}

    def save(self,commit=True):
        user=super().save(commit=False)
        user.password=make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        password1=cleaned_data.get('password')
        password2=cleaned_data.get('ConfirmPassword')
        if password1 != password2:
            self.add_error('ConfirmPassword', "Password Mismatch")
        return cleaned_data
    
class UserTypeForm(forms.ModelForm):
    class Meta:
        model=UserTypeModel
        fields=['usertype']
        labels={'usertype':'What Type of User You Are?'}
        user_types=[('Patient','Patient'),('Doctor','Doctor')]
        widget={'usertype':forms.RadioSelect(choices=user_types)}