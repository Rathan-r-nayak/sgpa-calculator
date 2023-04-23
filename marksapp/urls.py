from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("",views.default,name="default"),
    path("sgpa/",views.sgpa,name="sgpa"),
    path("cgpa/",views.cgpa,name="cgpa"),
    path("cgpa/action",views.cgpaInp,name="cgpa_inp"),
    path("sgpa/action",views.sgpaInp,name="sgpa_inp"),
]
