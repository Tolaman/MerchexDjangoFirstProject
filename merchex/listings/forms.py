from django import forms

from listings.models import Band
from listings.models import Title

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        # "fields = '__all__'" to celete every field, but we won't
        exclude = ('active', 'offical_homepage')

class ListingForm(forms.ModelForm):
    class Meta:
        model = Title
        exclude = ('sold',)
