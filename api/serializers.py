from rest_framework.serializers import ModelSerializer
from .models import Student


class StudentSerializer(ModelSerializer):
	class Meta:
		model = Student
		fields = ['first_name', 'last_name','gender', 'roll_no']
