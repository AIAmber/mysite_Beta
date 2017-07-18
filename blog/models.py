from django.db import models

# Create your models here.
class Category(models.Model):
    '''
    Classifacation
    '''

    name = models.CharField('Name', max_length=16)

class Tag(models.Model):
    '''
    Tag
    '''

    name = models.CharField('Name', max_length=16)

class Blog(models.Model):
    '''
    Blog
    '''

    title = models.CharField('Title', max_length=32)
    author = models.CharField('Author', max_length=16)
    content = models.TextField('Content')
    created = models.DateTimeField('Created Time', auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='Class')
    tags = models.ManyToManyField(Tag, verbose_name='Tag')

class Comment(models.Model):
    '''
    Comment
    '''

    blog = models.ForeignKey(Blog, verbose_name='Blog')

    name = models.CharField('Name', max_length=64)
    email = models.EmailField('Email')
    content = models.CharField('Content', max_length=255)

    created = models.DateTimeField('Created Time', auto_now_add=True)