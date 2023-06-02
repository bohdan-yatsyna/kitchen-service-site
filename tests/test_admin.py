from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="Test_superuser",
            password="12sdfEFffe32!",
        )

        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="Test_cook",
            password="Test_pass223",
            first_name="First",
            last_name="Cook",
            years_of_experience=3,
        )

    def test_cook_years_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_changelist")
        response_ = self.client.get(url)

        self.assertContains(response_, "Years of experience")
        self.assertContains(response_, self.cook.years_of_experience)

    def test_add_fieldsets_for_new_cook(self):
        url = reverse("admin:kitchen_cook_add")
        response_ = self.client.get(url)

        self.assertContains(response_, "First name:")
        self.assertContains(response_, "Last name:")
        self.assertContains(response_, "Years of experience")
