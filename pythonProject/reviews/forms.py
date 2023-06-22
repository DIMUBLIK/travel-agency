from .models import FeedBack
from django.forms import ModelForm, TextInput, DateInput,Textarea,NumberInput


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ['Name', 'Place', 'full_text', 'date', 'score']

        widgets = {
            "Name": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ваше имя'
            }),
            "Place": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место путешествия'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата путешествия'
            }),
            "score": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст отзыва'
            }),
        }