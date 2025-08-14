from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Course, Enrollment, Student
from .serializers import (RegisterSerializer, CourseSerializer, EnrollmentSerializer, StudentSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import LoginSerializer




# User Registration
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# List all courses
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

# Enroll in course
from rest_framework.views import APIView
from rest_framework import status

class EnrollView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        course_id = request.data.get('course_id')

        try:
            student = Student.objects.get(user=user)
            course = Course.objects.get(id=course_id)
            enrollment, created = Enrollment.objects.get_or_create(student=student, course=course)
            if created:
                return Response({'message': 'Enrolled successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Already enrolled.'}, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
        

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
        
#         token = super().get_token(user)
#         # Add custom claims if needed, e.g.:
#         token['username'] = user.username
#         return token

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
