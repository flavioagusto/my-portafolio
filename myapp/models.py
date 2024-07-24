from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_name = models.CharField(max_length=200)
    blog_content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.blog_name   