from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student


@api_view(['GET'])
def index(request):
	no_of_stds = Student.objects.all().count()
	return Response({'No. of students': no_of_stds})