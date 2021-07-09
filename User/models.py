from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetail(models.Model):
    firstname=models.CharField(max_length=225)
    lastname=models.CharField(max_length=225)
    email=models.EmailField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class PostDetail(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(blank=True, null=True)
    updated_at=models.DateTimeField(blank=True, null=True)

    def pub_date_pretty1(self):
        return self.created_at.strftime('%b %e %y')

    def pub_date_pretty2(self):
        return self.updated_at.strftime('%b %e %y')
