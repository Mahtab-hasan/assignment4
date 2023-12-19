from django import forms
from .models import MyModel
from django.forms.widgets import NumberInput


class ExamplateForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField()
    agree = forms.BooleanField()
    birth_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = "__all__"


class ExampleForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)


class ExampleForm2(forms.Form):
    agree = forms.BooleanField()


class Datetimes(forms.Form):
    birth_date = forms.DateField()


FAVORITE_COLORS_CHOICES = [
    ("blue", "Blue"),
    ("green", "Green"),
    ("black", "Black"),
]


class ChangingColor(forms.Form):
    favorite_colors = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
