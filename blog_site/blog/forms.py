from django import forms
from blog.models import Post,Comment
from django.contrib.auth.models import User
from blog.models import UserProfileInfo


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','title','text','image')

        widgets = {
            'author':forms.TextInput(attrs={'class':' editable medium-editor-textarea textinput '}),
            'title':forms.TextInput(attrs={'class':' editable medium-editor-textarea textinput '}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent ','rows':"2" ,'cols':"200"}),
        }

class CommentForm(forms.ModelForm):
     class Meta:
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':' editable medium-editor-textarea textinput'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea comment-text'})
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

        widgets = {
            'username':forms.TextInput(attrs={'class':'signup-form-input'}),
            'email':forms.EmailInput(attrs={'class':'signup-form-input'}),
            'password':forms.PasswordInput(attrs={'class':'signup-form-input'}),
            'confirm_password':forms.PasswordInput(attrs={'class':'signup-form-input'}),   
        }

        def clean(self):
            cleaned_data = super(UserForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError(
                    "password and confirm_password does not match"
                )

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
        widgets = {
            'profile_pic':forms.FileInput(attrs={'class':'image-btn'}),
        }