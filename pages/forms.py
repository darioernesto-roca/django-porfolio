from django import forms

from pages.models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ("name", "email", "subject", "message")
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control border rounded", "placeholder": "Your name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control border rounded", "placeholder": "Your email"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control border rounded", "placeholder": "Subject"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control border rounded",
                    "placeholder": "Your message",
                    "rows": 5,
                    "maxlength": 2000,
                    "x-model": "message",
                }
            ),
        }
