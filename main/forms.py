from django import forms
from .models import Tag, SetupPosts

class CreateNewPostForm(forms.ModelForm):
    tegs = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    class Meta:
            model = SetupPosts
            fields= ['title', 'main_photo', 'more_photo1', 'more_photo2', 'more_photo3', 'cpu', 'gpu', 'ram', 'ssd', 'monitor', 'ps', 'comment', 'story_setup', 'tegs']

          