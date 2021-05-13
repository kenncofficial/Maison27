from django import forms
from .models import BlogComment, Category, BlogPost, General_Supplies, Supply_Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

#general supplies 

options = Supply_Category.objects.all().values_list('name', 'name')

option_list = []

for supply in options:
    option_list.append(supply)



class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','image', 'blog_quote', 'category', 'subtitle', 'author',\
                   'content',  'writers_name', 'writers_summery', 'side_summery',  'facebook_url', 'instagram_url', 'twitter_url' )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),

            #'author': forms.Select(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'writers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'writers_summery': forms.Textarea(attrs={'class': 'form-control'}),
            'side_summery': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','image', 'blog_quote','category', 'subtitle',\
                   'content',  'writers_name', 'writers_summery', 'side_summery',  'facebook_url', 'instagram_url', 'twitter_url' )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'writers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'writers_summery': forms.Textarea(attrs={'class': 'form-control'}),
            'side_summery': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('content',)

        widgets = {
        'content': forms.Textarea(attrs={'class': 'form-control'})
        }

class AddSupplyForm(forms.ModelForm):
    class Meta:
        model = General_Supplies
        fields = ('name', 'image', 'supply_category', 'Description')

        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'supply_category': forms.Select(choices=option_list, attrs={'class': 'form-control'}),
        'Description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditSupplyForm(forms.ModelForm):
    class Meta:
        model = General_Supplies
        fields = ('name', 'image', 'supply_category', 'Description')

        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'supply_category': forms.Select(choices=option_list, attrs={'class': 'form-control'}),
        'Description': forms.Textarea(attrs={'class': 'form-control'}),
        }