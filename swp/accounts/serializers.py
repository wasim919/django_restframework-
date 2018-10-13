from .models import StudentProfile

from rest_framework import serializers

# class FoodOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FoodOrder
#         fields = '__all__'

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
