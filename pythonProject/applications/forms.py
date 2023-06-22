from .models import Applications
from django.forms import ModelForm, TextInput,Textarea,NumberInput


class ApplicationsForm(ModelForm):
    class Meta:
        model = Applications
        fields = ['Name', 'Place', 'PersonsCount', 'days', 'budget', 'text', 'mail']

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
            "budget": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Бюджет'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Пожелания'
            }),
            "mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
        }
