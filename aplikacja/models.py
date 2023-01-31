from django.db import models
from django.contrib.auth.models import User


PROFILE_STATUS = (
    ('unfollowed', 'Unfollowed'),
    ('followed', "Followed")
)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_name = models.TextField(max_length = 50)
    age = models.IntegerField()
    bio = models.TextField(max_length= 200)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    status = models.CharField(choices=PROFILE_STATUS, max_length=30, default='unfollowed')

    def __str__(self):
        return self.user_name


class Post(models.Model):
    picture = models.ImageField(upload_to='pics/', null=True, blank=True)
    description = models.TextField(max_length=400)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='photo_post')

    def __str__(self):
        return self.description

    def total_likes(self):
        return self.likes.count()       # działa poprawnie chociaż python pokazuje błąd

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, default=1)
    text = models.TextField(max_length=500)
    image = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.text
