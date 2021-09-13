from django.urls import path
from .views import index, StudentListView,StudentDetailView

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('student-detail/<int:pk>', StudentDetailView.as_view(), name='student-detail'),
    path('counts', index, name='counts'),
]