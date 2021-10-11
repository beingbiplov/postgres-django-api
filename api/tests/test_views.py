from django.test import TestCase
from api.views import index
from django.urls import reverse
from api.models import Student

class IndexViewTest(TestCase):

	def test_url_exists(self):
		response = self.client.get('/api/')
		self.assertEqual(response.status_code, 200)


	def test_view_url_accessibilty_by_name(self):
		response = self.client.get(reverse('student-list'))
		self.assertEqual(response.status_code, 200)