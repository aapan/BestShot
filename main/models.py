from django.db import models

from django.contrib import admin
from django.contrib.auth.models import User
from .storage import ImageStorage
from .otherFunctions.listField import ListField


# Create your models here.
# QuerySet 語法 - all()， get()， filter() 和 exclude()

class Classification(models.Model):
    name = models.CharField(primary_key=True, max_length=150)

    def __str__(self):
        return self.name


class Img(models.Model):
    # 每張img要有自己的id
    id = models.CharField(primary_key=True, max_length=20, null=False)
    image = models.ImageField(null=True, upload_to='img', storage=ImageStorage())
    cmpScore = models.FloatField(null=True)
    like = models.IntegerField(null=True)
    description = models.TextField(null=True)
    createTime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imgs')
    userLike = models.ManyToManyField(User, related_name="likeimgs")
    label = ListField(null=True)
    tagClass = models.ManyToManyField(Classification, related_name="imgs")

    def __str__(self):
        return self.id


class Comment(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    content = models.TextField()
    createTime = models.DateTimeField(auto_now=True)
    img = models.ForeignKey(Img, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.id


class UserProfile(models.Model):
    userProfile = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=30, null=True)
    historyImgs = models.ManyToManyField(Img, related_name='viewed_users')
    proPicture = models.ImageField(null=True, upload_to='img', storage=ImageStorage())
    biography = models.TextField(null=True)

    def __str__(self):
        return self.userProfile.username



