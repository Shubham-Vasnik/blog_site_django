from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='post_imgs',blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approve_comment=True)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()
    
    def get_absolute_url(self):
        return reverse('blog:post_list')

    def __str__(self):
        return self.text


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='info')

    profile_pic = models.ImageField(upload_to='profile_pics',default='profile_pics/default_profile_pic.jpg',blank=True)

    def __str__(self):
        return self.user.username