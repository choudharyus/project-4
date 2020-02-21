from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Patient
from django.contrib.auth.decorators import login_required
from .forms import PatientForm


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patientportal/patient_list.html', {'patients': patients})


def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patientportal/patient_form.html', {'form': form})


def patient_edit(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patientportal/patient_form.html', {'form': form})

