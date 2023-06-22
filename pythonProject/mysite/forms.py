from .models import Application
from django.forms import ModelForm, TextInput, NumberInput


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['Name', 'Place', 'PersonsCount', 'days', 'budget']

        widgets = {
            "Name": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ваше имя'
            }),
            "Place": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место путешествия'
            }),
            "PersonsCount": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество людей'
            }),
            "days": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество дней'
            }),

            "'budget'": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Бюджет'
            }),
        }