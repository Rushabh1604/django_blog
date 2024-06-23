from django.db import models

from django.contrib.auth.models import User
# Create your models here.


#----mycode


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)# change every time
    created = models.DateTimeField(auto_now_add=True) #one time

    class Meta:
        ordering = ['-updated', '-created']  #- will make them in decending order


    def __str__(self):
        return self.name


class Message(models.Model):
    users = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)# change every time
    created = models.DateTimeField(auto_now_add=True) #one time

    def __str__(self):
        return self.body[0:50]