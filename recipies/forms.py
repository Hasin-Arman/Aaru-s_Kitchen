from django import forms
from .models import recipyModel
class recipyForm(forms.ModelForm):
    class Meta:
        model=recipyModel
        exclude = ['slug']