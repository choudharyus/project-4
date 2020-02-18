from django.shortcuts import render

from .models import Patient

def patient_list(request):
    patient = Patient.objects.all()
    return render(request, 'patientportal/patient_list.html', {'patient': patient})


def login_page(request):
    return render(request, 'patientportal/login_page.html', {'name': 'Shahzad Choudhary'})