from django.urls import path
from .import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('patient/new', views.patient_create, name='patient_create'),
    path('patient/<int:pk>/edit', views.patient_edit, name='patient_edit'),

]
