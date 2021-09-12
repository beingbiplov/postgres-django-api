from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializer
from .models import Student


@api_view(['GET'])
def index(request):
	no_of_stds = Student.objects.all().count()
	return Response({'No. of students': no_of_stds})


class StudentListView(ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


class StudentDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer