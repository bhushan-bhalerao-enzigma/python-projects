from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['FirstName', 'LastName', 'Email','MobileNo'] 
        labels = {
        "FirstName": "First Name",
        "LastName": "Last Name",
        "Email": "Email",
        "MobileNo": "Mobile Number"
        }  