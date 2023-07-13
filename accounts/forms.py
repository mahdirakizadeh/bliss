from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput, min_length=6)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput, min_length=6)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'avatar')

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password <a href=\"../password/\">here</a>")

    class Meta:
        model: User
        fields = ('email', 'phone_number', 'full_name', 'avatar', 'password', 'last_login')


class UserSignupForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'book_n'}))
    full_name = forms.CharField(label='full name', widget=forms.TextInput(attrs={'class': 'book_n'}))
    phone = forms.CharField(max_length=11, widget=forms.NumberInput(attrs={'class': 'book_n'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'book_n'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'book_n'}))

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("this email already used")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError("this phone number already used")
        return phone


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()


class UserLoginForms(forms.Form):
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form_control, book_n'}),
                            max_length=12)
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form_control, book_n'}))
