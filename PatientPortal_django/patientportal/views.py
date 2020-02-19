from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Patient
from django.contrib.auth.decorators import login_required


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patientportal/patient_list.html', {'patients': patients})

