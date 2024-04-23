from django.test import TestCase
from django.urls import reverse
from .models import Departments, Employees

class DepartmentViewsTestCase(TestCase):
    def setUp(self):
        Departments.objects.create(department_id=1, department_name="IT")
        Departments.objects.create(department_id=2, department_name="HR")

    def test_department_list_view(self):
        response = self.client.get(reverse('department_get'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "IT")
        self.assertContains(response, "HR")

    def test_department_detail_view(self):
        response = self.client.get(reverse('department_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "IT")

    def test_department_post_view(self):
        data = '{"department_name": "Finance"}'  
        response = self.client.post(reverse('department_post'), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Added Successfully")

    def test_department_update_view(self):
        data = {'department_name': 'Finance'}
        response = self.client.put(reverse('department_update', args=[1]), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Updated Successfully")

    def test_department_delete_view(self):
        data = '{"employee_name": "Adam Johnson"}' 
        response = self.client.delete(reverse('department_delete', args=[1]), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Deleted Successfully")

    # Add more test methods for other views as needed

class EmployeeViewsTestCase(TestCase):
    def setUp(self):
        Employees.objects.create(employee_id=1, employee_name="John Doe", department="IT", date_of_joining="2024-04-23", photo_file_name="john.jpg")
        Employees.objects.create(employee_id=2, employee_name="Jane Smith", department="HR", date_of_joining="2024-04-24", photo_file_name="jane.jpg")

    def test_employee_list_view(self):
        response = self.client.get(reverse('employee_get'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertContains(response, "Jane Smith")

    def test_employee_detail_view(self):
        response = self.client.get(reverse('employee_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")

    def test_employee_post_view(self):
        data = '{"employee_name": "Adam Smith", "department": "Finance", "date_of_joining": "2024-04-25", "photo_file_name": "adam.jpg"}'
        response = self.client.post(reverse('employee_post'), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Added Successfully")

    def test_employee_update_view(self):
        data = '{"employee_name": "Adam Smith", "department": "HR", "date_of_joining": "2023-04-25", "photo_file_name": "smith.jpg"}'
        response = self.client.put(reverse('employee_update', args=[1]), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Updated Successfully")

    def test_employee_delete_view(self):
        response = self.client.delete(reverse('employee_delete', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Deleted Successfully")
