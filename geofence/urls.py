from django.urls import path
from geofence import views

urlpatterns = [
    path('home', views.StudentView.as_view(),name='home'),
    path('register', views.register),
    path('inout', views.inout),
    path('studententry', views.studententry),



]