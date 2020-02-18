from django import forms


class ExpertForm(forms.Form):

    name = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    personal_website_url = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "https://personalwebsite.com"}
        ),
    )
