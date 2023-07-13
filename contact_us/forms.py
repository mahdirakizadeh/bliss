from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label='Full name', max_length=50,
                                widget=forms.TextInput(attrs={'class': 'contactus', 'type': 'type'}))
    email = forms.EmailField(label='Email Address',
                             widget=forms.EmailInput(attrs={'class': 'contactus', 'type': 'type'}))
    phone_number = forms.CharField(label='Phone Number',
                                   widget=forms.TextInput(attrs={'class': 'contactus', 'type': 'type'}), max_length=11)
    message = forms.CharField(label='Message', max_length=2000, widget=forms.Textarea(attrs={'class': 'textarea'}))
