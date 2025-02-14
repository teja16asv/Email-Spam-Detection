from django import forms

class Messageform(forms.Form):
    text=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message here...' }))
    