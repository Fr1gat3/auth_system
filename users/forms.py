from django import forms


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form__input', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__input', 'placeholder': 'Password'}))


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Last Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form__input', 'placeholder': 'Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'Confirm Password'}))
