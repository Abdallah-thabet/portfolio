from django import forms


def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    bootfield = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty", validators=[should_be_empty])