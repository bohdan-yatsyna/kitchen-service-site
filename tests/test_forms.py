from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.forms import (
    CookCreationForm,
    CookUpdateForm,
    DishSearchForm,
    DishTypeSearchForm,
    CookSearchForm,
)
from kitchen.models import Dish, DishType


class CookCreateAndUpdateFormsTests(TestCase):
    def test_cook_create_form_with_data_is_valid(self):
        cook_data = {
            "email": "test@test.com",
            "username": "userzero",
            "first_name": "One Old",
            "last_name": "Two Young",
            "password1": "Tree12344",
            "password2": "Tree12344",
            "years_of_experience": 3,
        }

        form = CookCreationForm(data=cook_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, cook_data)

    def test_refuse_cook_create_form_with_data_is_not_valid(self):
        cook_data = {
            "email": "ttest@test.com",
            "username": "Uuserzero",
            "first_name": "The One",
            "last_name": "The Two",
            "password1": "Tree12344",
            "password2": "Tree12344",
            "years_of_experience": -3,
        }

        form = CookCreationForm(data=cook_data)
        self.assertNotEqual(form.is_valid(), True)

    def test_cook_update_form(self) -> None:
        new_data = {
            "first_name": "Two Old",
            "last_name": "One Young",
            "email": "tester@tester.com",
            "years_of_experience": 12,
        }

        form = CookUpdateForm(data=new_data)
        self.assertEqual(form.data, new_data)


class SearchFormsTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="Admin123",
            password="TestPas2345"
        )
        self.client.force_login(self.user)

        self.dish_type_one = DishType.objects.create(
            name="Pizza",
        )
        self.dish_type_two = DishType.objects.create(
            name="Pasta",
        )

    def test_dish_search_form_get_correct_result(self):
        self.car1 = Dish.objects.create(
            name="Margarita",
            price=123.11,
            dish_type=self.dish_type_one,
        )
        self.car2 = Dish.objects.create(
            name="Karbonara",
            price=145.71,
            dish_type=self.dish_type_two,
        )

        url = reverse("kitchen:dish-list")
        dish_search_data = {"name": "Karb"}

        response = self.client.get(url, data=dish_search_data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context["search_form"],
            DishSearchForm,
        )
        self.assertEqual(
            response.context["search_form"].initial["name"],
            "Karb",
        )

    def test_dish_type_search_form_get_correct_result(self):
        url = reverse("kitchen:dish-type-list")
        dish_type_search_data = {"name": "Pasta"}

        response = self.client.get(url, data=dish_type_search_data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context["search_form"],
            DishTypeSearchForm,
        )
        self.assertEqual(
            response.context["search_form"].initial["name"],
            "Pasta",
        )

    def test_cook_search_form_get_correct_result(self):
        self.cook_one = get_user_model().objects.create_user(
            username="Admin_one",
            password="Qwert123",
            years_of_experience=7,
        )
        self.cook_two = get_user_model().objects.create_user(
            username="Second",
            password="super.cook",
            years_of_experience=13,
        )

        url = reverse("kitchen:cook-list")
        cook_search_data = {"username": "admin"}

        response = self.client.get(url, data=cook_search_data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context["search_form"],
            CookSearchForm,
        )
        self.assertEqual(
            response.context["search_form"].initial["username"],
            "admin",
        )
