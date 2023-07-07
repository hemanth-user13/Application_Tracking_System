import unittest
from django.test import Client
from django.shortcuts import reverse
from .models import Candidate, Cse, Civil, Mechanical, Ece, Eee
from . import views


class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details_view(self):
        response = self.client.get(reverse('details'))
        self.assertEqual(response.status_code, 200)

    def test_login_val_with_invalid_credentials(self):
        response = self.client.post(reverse('login_val'), {'username': 'invalid', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')

    def test_login_val_with_valid_credentials(self):
        # Assuming a valid username and password exist in the database
        candidate_signup = Candidate.objects.create(username='validuser', password='validpassword')
        response = self.client.post(reverse('login_val'), {'username': 'validuser', 'password': 'validpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_excel_view_get(self):
        response = self.client.get(reverse('excel'))
        self.assertEqual(response.status_code, 200)

    # Add more tests for the excel view based on your requirements

    def test_add_candidate_view_post(self):
        response = self.client.post(reverse('add_candidate'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'branch': 'CSE',
            'skills': 'Python, Django',
            'jr_number': '12345',
            'phone_number': '1234567890',
            'email_address': 'john.doe@example.com',
            'current_company': 'ABC Corp',
            'total_experience': '5 years',
            'ctc': '10 LPA',
            'expected_ctc': '12 LPA',
            'offers_in_hand': '2',
            'notice_period': '30 days',
            'current_location': 'City A',
            'source': 'Job Portal',
            'screening_status': 'Pending',
            'screened_by': 'Admin'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

        # Verify if the candidate and Cse objects are created
        candidate = Candidate.objects.get(first_name='John', last_name='Doe')
        cse = Cse.objects.get(first_name='John', last_name='Doe')
        self.assertIsNotNone(candidate)
        self.assertIsNotNone(cse)

        # Add more assertions based on your requirements

    # Add more tests for the remaining views

    def test_option_view_post(self):
        response = self.client.post(reverse('option'), {'visualization': 'Registrationform'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

        response = self.client.post(reverse('option'), {'visualization': 'Excel'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excel.html')

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    # Add more tests for the remaining views

    def test_candidate_list_view(self):
        response = self.client.get(reverse('candidate_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'candidate_list.html')

    # Add more tests for the remaining views

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
