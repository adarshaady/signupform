from django import forms

from myapp.models import Registration

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
