from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
CHOICES = [("Arts", "Arts"), ("Technology", "Technology")]
class Post(models.Model):
    """
    Class represents the categories model
    """
    title = models.CharField(max_length=280, unique=True)
    slug = models.SlugField(max_length=280, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    featured_image = CloudinaryField('image', default='placeholder')
    category = models.CharField(max_length=250, choices=CHOICES)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)


    class Meta:
        """
        This shows comments in decending order
        """
        ordering = ['-created_on']

    def _str_(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    """
    This class represents the comments model
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                 related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta():
        ordering = ["created_on"]

    def _str_(self):
        return f"Comment {self.body} by {self.name}"
