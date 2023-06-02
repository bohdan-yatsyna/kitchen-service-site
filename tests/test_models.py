from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType


class ModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(
            name="DisTestType"
        )

        self.cook = get_user_model().objects.create_user(
            username="Test username",
            first_name="Name first",
            last_name="Name last",
            password="Test_12345",
            years_of_experience=3,
        )

        self.dish = Dish.objects.create(
            name="some strange dish",
            description="Strange taste",
            price=111.00,
            dish_type=self.dish_type,
        )

        self.dish.cooks.set([self.cook])

    def test_cook_str(self):
        self.assertEqual(
            str(self.cook),
            f"{self.cook.username}"
            f" ({self.cook.first_name}"
            f" {self.cook.last_name})",
        )

    def test_cook_get_absolute_url(self) -> None:
        url = self.cook.get_absolute_url()

        test_url = reverse(
            "kitchen:cook-detail",
            kwargs={"pk": self.cook.pk},
        )
        self.assertEqual(url, test_url)

    def test_cook_years_of_experience(self) -> None:
        self.assertEqual(self.cook.username, "Test username")
        self.assertTrue(self.cook.check_password("Test_12345"))
        self.assertEqual(self.cook.years_of_experience, 3)

    def test_dish_str(self):
        self.assertEqual(
            str(self.dish),
            f"{self.dish.name}, "
            f"price: {self.dish.price},"
            f" type: {self.dish.dish_type.name}",
        )

    def test_dish_type_str(self):
        self.assertEqual(str(self.dish_type), self.dish_type.name)
