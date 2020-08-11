from django import forms
from django.forms import ValidationError
from .models import SimpleForm

class SimpleForm(forms.ModelForm):
    name = forms.CharField(label = 'Name')
    email = forms.EmailField(label = 'E-mail')
    mobile = forms.IntegerField( label = 'Mobile')
    address = forms.CharField(label = 'Address', required=False)
    city = forms.CharField()
    state = forms.CharField()

    class Meta:
        model = SimpleForm
        fields = '__all__'

#Validation for email and Mobile
    def valmobile(self):
        mobile = self.cleaned_data['mobile']
        if len(mobile)<10:
            raise forms.ValidationError("Mobile no, should be less than 10 digit")
        return mobile

    def valemail(self):
        email = self.cleaned_data['email']
        if not email.endswitch('@gmail.com'):
            raise forms.ValidationError("Enter proper email domain")
        return email
