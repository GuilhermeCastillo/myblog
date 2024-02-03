from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, related_name="article_tag")
    date = models.DateField()
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    photo =  models.ImageField(upload_to="articles", blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    email = models.CharField(max_length=200)