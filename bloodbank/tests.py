
from django.test import TestCase
from django.urls import reverse
from .models import DonorScreening


class BloodbankTests(TestCase):

    def test_dashboard_loads(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_donor_page_loads(self):
        response = self.client.get(reverse('donors'))
        self.assertEqual(response.status_code, 200)

    def test_donor_add_page_loads(self):
        response = self.client.get(reverse('donor_add'))
        self.assertEqual(response.status_code, 200)

    def test_donor_creation(self):
        donor = DonorScreening.objects.create(
            full_name='Test Donor',
            age=24,
            phone='9876543210',
            blood_group='O+',
            screening_date='2026-10-12',
            screening_status='Eligible',
        )

        self.assertEqual(donor.full_name, 'Test Donor')
        self.assertEqual(DonorScreening.objects.count(), 1)

