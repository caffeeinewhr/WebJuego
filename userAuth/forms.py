from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True, 
        label='Username', 
        widget=forms.TextInput({
            'class':'form-control',
            'placeholder':'username'
        })
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput({
            'class':'form-control',
            'placeholder':'email'
        })
    )
    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput({
            'class':'form-control',
            'placeholder':'password'
        })
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, 
        label='Username', 
        widget=forms.TextInput({
            'class':'form-control',
            'placeholder':'username'
        })
    )
    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput({
            'class':'form-control',
            'placeholder':'password'
        })
    )
