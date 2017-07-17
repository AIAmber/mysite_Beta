from django import forms

class CommentForm(forms.Form):
    '''
    Comment Form
    '''

    name = forms.CharField(label='Name', max_length=16, error_messages={
        'required': 'Please input your name!',
        'max_length': 'Your name is too long!',
    })

    email = forms.EmailField(label='Email', error_messages={
        'required': 'Please input your email!',
        'invalid': 'The form of your email is error!',
    })

    content = forms.CharField(label='Content',max_length=140, error_messages={
        'required': 'Please input your content!',
        'max_length': 'Your content is too long!',
    })