from django import forms
from .models import Listing
from users.models import Location


class ListingForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'mileage', 'color', 'description', 'engine', 'transmission', 'image',}


class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    lga = forms.CharField(required=True)
    state = forms.CharField(required=True)

    class Meta:
        model=Location
        fields = {'state', 'city', 'address_1', 'address_2', 'lga'}