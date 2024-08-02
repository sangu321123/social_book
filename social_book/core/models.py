from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
import uuid #to generate unique if for post
User=get_user_model()#to get model of the currently authentiacted(logged in) user.we get the foreign key
# Create your models here.
class Profile(models.Model):#table in db
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  id_user=models.IntegerField()
  bio=models.TextField(blank=True)#blank true should be mentioned explicitly
  profileimg=models.ImageField(upload_to='profile_images',default="blank-profile-picture-973460_1280.png")#for the firstime django itself creates profile_images folder
  location=models.CharField(max_length=100,blank=True)

  def __str__(self):
    return self.user.username
  
class Post(models.Model):
  id=models.UUIDField(primary_key=True,default=uuid.uuid4)#when set as primary key it replaces the original id given by django and it appears in url as well
  user=models.CharField(max_length=100)
  image=models.ImageField(upload_to="post_images")
  caption=models.TextField()
  created_at=models.DateTimeField(default=datetime.now)
  no_of_likes=models.IntegerField(default=0)

  def __str__(self):
    return self.user

class LikePost(models.Model):
  post_id=models.CharField(max_length=100)
  username=models.CharField(max_length=100)

  def __str__(self):
    return self.username

class FollowerCount(models.Model):
  follower=models.CharField(max_length=100)
  user=models.CharField(max_length=100)

  def __str__(self):
    return self.user
  