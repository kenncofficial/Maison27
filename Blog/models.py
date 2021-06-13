from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField

# Create your models here.
class Home_Layout(models.Model):
    home_title = models.CharField(max_length=255)
    home_discription = models.CharField(max_length=455)

class About(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)

class Supply_Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class General_Supplies(models.Model):
    name = models.CharField(max_length=255)
    image = CloudinaryField('image', null=True, blank=True)
    supply_category = models.CharField(max_length=255, default='uncategorize')
    Description = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Main_Service(models.Model):
    service_title = models.CharField(max_length=255)
    service_content = models.CharField(max_length=255)
    full_service_discription = RichTextField(blank=False)

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    Email = models.EmailField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User_Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = CloudinaryField('image', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='uncategorize')
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True)
    blog_quote = models.CharField(max_length=500, blank=True)
    facebook_url = models.URLField(max_length=255, null=True, blank=True)
    instagram_url = models.URLField(max_length=255, null=True, blank=True)
    twitter_url = models.URLField(max_length=255, null=True, blank=True)
    gmail_url = models.URLField(max_length=255, null=True, blank=True)
    writers_name =  models.CharField(max_length=200, default='Admin')
    writers_summery = models.TextField(default='I hope this article was helpful to you, Thank you')
    side_summery = models.CharField(max_length=600)
    
   
    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('BlogPost-details', kwargs={'pk': self.pk})

class   BlogComment(models.Model):
    blogpost_connected =  models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.author) + ' , ' + self.blogpost_connected.title[:40]

    def get_absolute_url(self):
        return reverse('update_comment', kwargs={'pk': self.pk})

