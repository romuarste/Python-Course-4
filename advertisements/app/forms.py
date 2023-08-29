from django import forms
from .models import Advertisement
from django.core import validators
from django.core.exceptions import ValidationError

def validate_question_mark(value):
    if value.startswith('?'):
        raise ValidationError(
            ('Название не должно начинаться со знака вопроса')
        )

class AdvertisementForm(forms.ModelForm):

    title = forms.CharField(
        validators=[validate_question_mark],
        label='Название',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        )

    class Meta:
        model = Advertisement
        
        exclude = ['user']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }


# from django import forms

# class AdvertisementForm (forms.Form):
#     title = forms.CharField(max_length=64, label="Название", widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     description  = forms.CharField(widget=forms.Textarea, label="Описание")
#     price = forms.DecimalField()
#     auction = forms.BooleanField(required=False)
#     image = forms.ImageField()
