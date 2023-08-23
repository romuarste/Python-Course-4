from django import forms

class AdvertisementForm (forms.Form):
    title = forms.CharField(max_length=64, label="Название", widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description  = forms.CharField(widget=forms.Textarea, label="Описание")
    price = forms.DecimalField()
    auction = forms.BooleanField(required=False)
    image = forms.ImageField()
