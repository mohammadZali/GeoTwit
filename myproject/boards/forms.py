from django import forms
from .models import Topic
from .models import Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What happened for you today(required)?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )
    # Adress = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={'rows': 5, 'placeholder': 'Where it was happened(required)?'}
    #     ),
    #     max_length=100,
    #     help_text='The max length of the text is 100.'
    # )
    image = forms.FileField(required=False,
                            help_text='Its optional')

    class Meta:
        model = Topic
        fields = ['subject', 'message','image']




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message',]