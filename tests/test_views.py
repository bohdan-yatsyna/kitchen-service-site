from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType


DISH_TYPE_URL = reverse("kitchen:dish-type-list")
DISH_URL = reverse("kitchen:dish-list")
COOK_URL = reverse("kitchen:cook-list")


class PublicCookTest(TestCase):
    def test_login_required(self):
        res = self.client.get(COOK_URL)

        self.assertNotEquals(res.status_code, 200)


class PublicDishTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_URL)

        self.assertNotEquals(res.status_code, 200)


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)

        self.assertNotEquals(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="Test_cook",
            password="Cook_12345",
        )

        self.client.force_login(self.cook)

    def test_create_cook(self):
        cook_data = {
            "username": "Cook-123",
            "first_name": "Cook_name",
            "last_name": "Cook_surname",
            "password1": "Test-098765",
            "password2": "Test-098765",
            "years_of_experience": 5,
        }

        self.client.post(reverse("kitchen:cook-create"), data=cook_data)
        new_cook = get_user_model().objects.get(
            username=cook_data["username"]
        )

        self.assertEqual(new_cook.first_name, cook_data["first_name"])
        self.assertEqual(new_cook.last_name, cook_data["last_name"])
        self.assertEqual(
            new_cook.years_of_experience,
            cook_data["years_of_experience"]
        )


class PrivateDishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "testUser1",
            "User_654321"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish(self):
        dish_type_one = DishType.objects.create(name="Dish1")
        dish_type_two = DishType.objects.create(name="Dish2")

        Dish.objects.create(
            name="Dish_1",
            price=123.11,
            dish_type=dish_type_one,
        )
        Dish.objects.create(
            name="Dish_2",
            price=145.99,
            dish_type=dish_type_two,
        )

        response_ = self.client.get(DISH_URL)
        dish = Dish.objects.all()

        self.assertEquals(response_.status_code, 200)
        self.assertEquals(
            list(response_.context["dish_list"]),
            list(dish)
        )
        self.assertTemplateUsed(response_, "kitchen/dish_list.html")


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "testUser2",
            "User_123456"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type(self):
        DishType.objects.create(name="Test_type1")
        DishType.objects.create(name="Test_type2")

        response_ = self.client.get(DISH_TYPE_URL)
        dish_types = DishType.objects.all()

        self.assertEquals(response_.status_code, 200)
        self.assertEquals(
            list(response_.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response_, "kitchen/dish_type_list.html")
