from django.test import TestCase
from api.models import Student

class StudentModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Student.objects.create(first_name='Adam', last_name='Smith', gender='Male', roll_no=1)

	def test_first_name_label(self):
		student = Student.objects.get(id=1)
		field_label = student._meta.get_field('first_name').verbose_name
		self.assertEqual(field_label, 'first name')

	def test_first_name_maxlength(self):
		student = Student.objects.get(id=1)
		max_length = student._meta.get_field('first_name').max_length
		self.assertEqual(max_length, 50)

	def test_object_name(self):
		student = Student.objects.get(id=1)
		expected_obj_name = f'{student.first_name} {student.last_name}'
		self.assertEqual(expected_obj_name, 'Adam Smith')
