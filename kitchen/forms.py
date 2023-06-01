from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from kitchen.models import Dish


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data["price"]

        if price < 0:
            raise ValidationError("Price has to be greater than 0.")

        return price
