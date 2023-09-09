from django import forms
from .models import recipyModel
class recipyForm(forms.ModelForm):
    class Meta:
        model=recipyModel
        fields=['title','ingredients','instructions','image','category']