from django import forms
from .models import Contact_us
    

class Contact_usCreate(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ('name','email_id','subject','contact_number','description')
