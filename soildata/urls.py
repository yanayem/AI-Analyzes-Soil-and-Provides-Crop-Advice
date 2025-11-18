from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'soildata'
urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),
]
