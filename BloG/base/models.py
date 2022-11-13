from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['updated_on']

class Blog(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    description=models.TextField()
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['updated_on']

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,default=None,related_name='comments')
    comment=models.TextField()
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment
    class Meta:
        ordering=['updated_on']