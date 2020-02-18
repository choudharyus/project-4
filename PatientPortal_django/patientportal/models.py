from django.db import models

class Patient(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    DOB = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    medication = models.CharField(max_length=500)
    diagnosis = models.CharField(max_length=1000)

    def __str__(self):
        return self.firstName + ", " + self.lastName