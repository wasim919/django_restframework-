# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import StudentProfile, FoodOrder
# from .serializers import StudentProfileSerializer
# from django.shortcuts import get_object_or_404
#
# @api_view(['GET', 'POST'])
# def student(request):
#     if request.method == 'GET':
#         students = StudentProfile.objects.all()
#         serializer = StudentProfileSerializer(students, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = StudentProfileSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def student_detail(request, pk, format = None):
#     student = get_object_or_404(StudentProfile, pk = pk)
#     if request.method == 'GET':
#         serializer = StudentProfileSerializer(student)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer =StudentProfileSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import StudentProfile
from django.shortcuts import get_object_or_404
from .serializers import StudentProfileSerializer

class get_students_list(APIView):
    def get(self, request):
        students = StudentProfile.objects.all()
        serializer = StudentProfileSerializer(students, many = True)
        return Response(serializer.data, status = 200)
    def post(self, request):
        serializer = StudentProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class get_students_detail(APIView):
    def get(self, request, pk):
        student = get_object_or_404(StudentProfile, pk = pk)
        serializer = StudentProfileSerializer(student)
        return Response(serializer.data, status = 200)

    def delete(self, request, pk):
        student = get_object_or_404(StudentProfile, pk = pk)
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        student = get_object_or_404(StudentProfile, pk = pk)
        serializer = StudentProfileSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
