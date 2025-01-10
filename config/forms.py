from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    terms_accepted = forms.BooleanField(required=True)


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2
    
    def clean(self):
        cleaned_data = super().clean()
        terms_accepted = cleaned_data.get('terms_accepted')
        if not terms_accepted:
            raise forms.ValidationError('Please accept the Terms of Use and Privacy Policy to continue.')
        return cleaned_data
    
    def save(self, commit=True):

        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password1'])

        if commit:
            user.save()
        return user