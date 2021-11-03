from __future__ import unicode_literals

from django.test import TestCase
from .models import neighbourhood
from django.contrib.auth.models import User
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.kinoo = neighbourhood(neighbourhood='kinoo')

    def test_instance(self):
        self.assertTrue(isinstance(self.kinoo,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.kinoo.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.kinoo.delete_neighbourhood('kinoo')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)
