from django.urls import path
from .views import index, StudentListView,StudentDetailView

urlpatterns = [
    path('', index, name='index'),
    path('student-list', StudentListView.as_view(), name='student-list'),
    path('student-detail/<int:pk>', StudentDetailView.as_view(), name='student-detail'),
]