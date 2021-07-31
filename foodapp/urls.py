from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.catfunction,name='catfunction'),
    path("<slug:c_slug>/",views.catfunction,name='cat_prod'),
    path("<slug:c_slug>/<slug:product_slug>/",views.profunction,name='profunction')
]