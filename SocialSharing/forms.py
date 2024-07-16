from django import forms
from .models import SharedContent

class SharedContentForm(forms.ModelForm):
    class Meta:
        model = SharedContent
        fields = ['title', 'content', 'image']
