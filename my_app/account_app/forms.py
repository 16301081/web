from django import forms


class RegisterFrom(forms.Form):
    email = forms.EmailField(required=True,widget=forms.EmailInput, error_messages={'invalid': 'enter a valid email address.'})
    username = forms.CharField(required=True,widget=forms.TextInput)
    password = forms.CharField(required=True,  widget=forms.PasswordInput)
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput)


class Changepswform(forms.Form):
    old_password = forms.CharField(required=True,  widget=forms.PasswordInput)
    password = forms.CharField(required=True,  widget=forms.PasswordInput)
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput)

class Weiboform(forms.Form):
    content=forms.CharField(required=True,widget=forms.TextInput,max_length=300)