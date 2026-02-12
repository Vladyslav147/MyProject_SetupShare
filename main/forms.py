from django import forms
from .models import Tag, SetupPosts,CommentPost

class CreateNewPostForm(forms.ModelForm):
    tegs = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    class Meta:
            model = SetupPosts
            fields= ['title', 'main_photo', 'more_photo1', 'more_photo2', 'more_photo3', 'cpu', 'gpu', 'ram', 'ssd', 'monitor', 'ps', 'comment', 'story_setup', 'tegs']

            widgets = {
                  'more_photo1': forms.FileInput(attrs={'class': 'gallery-input'}),
                  'more_photo2': forms.FileInput(attrs={'class': 'gallery-input'}),
                  'more_photo3': forms.FileInput(attrs={'class': 'gallery-input'}),


                  'main_photo': forms.FileInput(attrs={'id': 'main_photo_input'}),
                  'title': forms.TextInput(attrs={'placeholder': 'Введите имя поста'}),
                  'cpu': forms.TextInput(attrs={'placeholder': 'Intel i5 10400f'}),
                  'gpu': forms.TextInput(attrs={'placeholder': 'RTX 4070'}),
                  'ram': forms.TextInput(attrs={'placeholder': '16'}),
                  'ssd': forms.TextInput(attrs={'placeholder': '1T'}),
                  'monitor': forms.TextInput(attrs={'placeholder': ' ACER 27 180Hz'}),
                  'ps': forms.TextInput(attrs={'placeholder': '500W'}),
                  'comment': forms.TextInput(attrs={'placeholder': 'Ещё корпус от Lian-Li'}),
                  'story_setup': forms.TextInput(attrs={'placeholder': 'История вашей сборки или же что хотите дополнить'}),
            }

            
class UpdatePostForm(forms.ModelForm):
    tegs = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    class Meta:
            model = SetupPosts
            fields= ['title', 'cpu', 'gpu', 'ram', 'ssd', 'monitor', 'ps', 'comment', 'story_setup', 'tegs']
            widgets = {
                  'title': forms.TextInput(attrs={'class': 'form-control'}),
                  'cpu': forms.TextInput(attrs={'class': 'form-control'}),
                  'gpu': forms.TextInput(attrs={'class': 'form-control'}),
                  'ram': forms.TextInput(attrs={'class': 'form-control'}),
                  'ssd': forms.TextInput(attrs={'class': 'form-control'}),
                  'monitor': forms.TextInput(attrs={'class': 'form-control'}),
                  'ps': forms.TextInput(attrs={'class': 'form-control'}),
                  'comment': forms.TextInput(attrs={'class': 'form-control'}),
                  'story_setup': forms.Textarea(attrs={'class': 'form-control'}),
            }

class CommentPostForm(forms.ModelForm):
      class Meta:
            model = CommentPost
            fields = ['text',]
            labels = {
                  'text': ''
            }
            widgets = {
                  'text': forms.Textarea(attrs={'rows': '2', 'placeholder': 'Оставьте свой отзыв о сетапе...'})
            }

          
