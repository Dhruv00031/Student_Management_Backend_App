from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

from .models import Student


class StudentAPITests(APITestCase):

    def setUp(self):
        # Create normal user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.user_token = Token.objects.create(user=self.user)

        # Create admin user
        self.admin = User.objects.create_superuser(
            username="adminuser",
            password="adminpass123"
        )
        self.admin_token = Token.objects.create(user=self.admin)

        # Sample student
        self.student = Student.objects.create(
            name="Test Student",
            roll_number="CS500",
            email="test500@test.com",
            course="B.Tech",
            year=3
        )

        self.list_url = "/api/v1/students/"
        self.detail_url = f"/api/v1/students/{self.student.id}/"

    # 1️⃣ Authenticated user can GET students
    def test_authenticated_user_can_view_students(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.user_token.key
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 2️⃣ Unauthenticated user cannot GET students
    def test_unauthenticated_user_cannot_view_students(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 3️⃣ Authenticated user can CREATE student
    def test_authenticated_user_can_create_student(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.user_token.key
        )
        data = {
            "name": "New Student",
            "roll_number": "CS501",
            "email": "new501@test.com",
            "course": "B.Tech",
            "year": 2
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # 4️⃣ Non-admin user cannot DELETE student
    def test_non_admin_cannot_delete_student(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.user_token.key
        )
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # 5️⃣ Admin user CAN DELETE student
    def test_admin_can_delete_student(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.admin_token.key
        )
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
