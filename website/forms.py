from django import forms


class EmailForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField()
    receiver = "chuckcwh@gmail.com"