from django import forms
from .models import Comment, Blog


class CommentForm(forms.Form):
    '''
    # Comment Form
    '''

    name = forms.CharField(label='Name', max_length=16, error_messages={
        'required': 'Please input your name!',
        'max_length': 'Your name is too long!',
    })

    email = forms.EmailField(label='Email', error_messages={
        'required': 'Please input your email!',
        'invalid': 'The form of your email is error!',
    })

    content = forms.CharField(label='Content', error_messages={
        'required': 'Please input your content!',
        #'max_length': 'Your content is too long!',
    })
    


'''
class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['Name', 'Email', 'Body']

        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Please input your name',
                'aria-decribedby': 'sizing-addon1',
            }),

            'Email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Please input your email',
                'aria-decribedby': 'sizing-addon1',
            }),

            'Content': forms.Textarea(attrs={'placeholder': 'Write to comment...'})
        }
'''