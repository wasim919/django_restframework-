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

class FoodOrder(models.Model):
    idfood_order = models.IntegerField(primary_key=True)
    student = models.ForeignKey('StudentProfile', on_delete = models.DO_NOTHING, blank=True, null=True)
    #food = models.ForeignKey('Menu', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    # timestamp = models.DateTimeField(blank=True, null=True)
    # created_at = models.DateField(blank=True, null=True)
    # created_by = models.CharField(max_length=45, blank=True, null=True)
    # modified_at = models.DateField(blank=True, null=True)
    # modified_by = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return str(self.student.first_name)
