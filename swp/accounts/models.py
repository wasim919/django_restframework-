from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 20, blank=True)
    gender_choices = (
    (MALE, 'Male'),
    (FEMALE, 'Female')
    )
    gender = models.CharField(max_length=2, choices = gender_choices, default = '')

    def __str__(self):
        return str(self.first_name)
