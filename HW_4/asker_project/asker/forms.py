from django import forms
from django.core.exceptions import ValidationError
from .models import User, Profile, Question, Tag, Answer

class LoginForm(forms.Form):
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    username = forms.CharField()

    def clean_password(self):
        data = self.cleaned_data['password']
        return data

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    password_check = forms.CharField(min_length=6, widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_check = cleaned_data.get('password_check')

        if password and password_check and password != password_check:
            self.add_error('password', 'Passwords do not match')
            self.add_error('password_check', 'Passwords do not match')
            raise ValidationError('Wrong password')

        return cleaned_data

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        avatar = self.cleaned_data.get('avatar')

        self.cleaned_data.pop('password_check')
        self.cleaned_data.pop('avatar')

        user = User.objects.filter(username=username)
        if user:
            self.add_error('username', 'User with this username already exists.')
            return None
        user = User.objects.filter(email=email)
        if user:
            self.add_error('email', 'User with this email already exists.')
            return None
        
        user = User.objects.filter(email=email, username=username)
        user = User.objects.create_user(**self.cleaned_data)
        profile = Profile.objects.create(user=user)
        if avatar is not None:
            profile.avatar = avatar
            profile.save()
        return user
    

class QuestionForm(forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea, max_length=5000)
    tags = forms.CharField(required=False, widget=forms.Textarea(), max_length=100)

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        tags = [tag for tag in tags.split()]
        return tags
    
    def clean(self):
        cleaned_data = super().clean()
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')
        tags = self.cleaned_data.get('tags', [])

        if(not title):
            self.add_error('title', 'This is required field')
            raise ValidationError('Field Title is not entered')
        if(not text):
            self.add_error('text', 'This is required field')
            raise ValidationError('Field Text is not entered')
        
        return cleaned_data
    
    def save(self, user):
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')
        tags = self.cleaned_data.get('tags')

        author = user.profile
        question = Question.objects.create(author=author, title=title, text=text)

        tags_list = []
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(title=tag_name)
            tags_list.append(tag)
        
        question.tags.set(tags_list)

        return question
    
class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=5000)

    def clean(self):
        cleaned_data = super().clean()
        text = self.cleaned_data.get('text')
        if(not text):
            self.add_error('text', 'This is required field')

        return cleaned_data
    
    def save(self, question, author):
        text = self.cleaned_data.get('text')
        answer = Answer.objects.create(author=author, question=question, text=text)
        return answer


class SettingsForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    username = forms.CharField(required=False)
    email = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        user_check = User.objects.exclude(pk=self.instance.pk).filter(username=username).exists()
        if user_check:
            self.add_error('username', 'This is login already exists')

        user_check = User.objects.exclude(pk=self.instance.pk).filter(email=email).exists()
        if user_check:
            self.add_error('email', 'This email already exists')

        return cleaned_data
    
    def save(self):
        user = super().save()
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            user.profile.avatar = self.cleaned_data.get('avatar')
            user.profile.save()        
        return user

        

        

