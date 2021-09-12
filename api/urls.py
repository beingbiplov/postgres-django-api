from django.urls import path
from .views import index, StudentListView

urlpatterns = [
    path('', index, name='index'),
    path('student-list', StudentListView.as_view(), name='student-list'),
]