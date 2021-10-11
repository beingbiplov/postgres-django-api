from django.test import TestCase
from api.views import index
from django.urls import reverse, include, path
from api.models import Student
from rest_framework import status
from api.serializers import StudentSerializer
from rest_framework.test import APITestCase, URLPatternsTestCase

class APITest(TestCase):

	def SetUp(self):
		Student.objects.create(first_name='Adam', last_name='Smith', gender='Male', roll_no=1)
		Student.objects.create(first_name='John', last_name='Doh', gender='Male', roll_no=2)
		Student.objects.create(first_name='Anna', last_name='Marie', gender='Female', roll_no=3)

	def test_all_data(self):
		response = self.client.get(reverse('student-list'))

		students = Student.objects.all()
		serializer = StudentSerializer(students, many=True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	

class StudentPostTest(APITestCase):

	def test_api_post(self):
		url = reverse('student-list')
		data = {'first_name':'John', 'last_name':'Doh', 'gender':'Male', 'roll_no':2}

		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Student.objects.count(), 1)
		self.assertEqual(Student.objects.get().first_name, 'John')
