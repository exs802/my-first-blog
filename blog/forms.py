from django import forms
from .models import Post, CVItem

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        
class CVForm(forms.ModelForm):
    class Meta:
        model = CVItem
        fields = ('title', 'text',)
     