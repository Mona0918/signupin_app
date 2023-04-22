from django.urls import path
from . import views

app_name='signupin'

urlpatterns=[
    path("",views.homeview,name="home"),
    path("usertype/",views.usertypeview,name="usertype"),
    path("signup/<str:type>/",views.signupview,name="signup"),
    path("signin/",views.loginview,name="signin"),
    path("dashboard/<str:name>/",views.dashboardview,name="dashboard"),
    path("signin/",views.logoutview,name="logout"),
]
