from django import forms
from users.models import CustomRegisterUser, BioUsers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}))

class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomRegisterUser
        fields = ['username', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'phone' in self.fields:
            self.fields['phone'].label = 'Номер телефона'

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['placeholder'] = ''
        
    def clean_email(self):
        email = self.cleaned_data.get('email')                                  # 1. Берем данные, которые Django уже признал похожими на email
        if CustomRegisterUser.objects.filter(email=email).exists():              # 2. Идем в базу данных и спрашиваем: "Уже есть такой?"
            raise forms.ValidationError("Пользователь с такой почтой уже есть!")# 3. Если ответ "Да", выбрасываем (raise) красную карточку
        return email                                                            # 4. Если всё ок, ОБЯЗАТЕЛЬНО возвращаем этот email обратно
    
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = BioUsers
        fields = ['background_image', 'first_name', 'profission', 'bio', 'Instagram_url', 'github_url', 'discord_url', 'steam_url', 'telegram_url', 'spotify_url', 'tiktok_url']

class LoadingUserAvatarForm(forms.ModelForm):
    class Meta:
        model = BioUsers
        fields = ['avatar']