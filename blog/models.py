from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo')

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = '1. Site'
    def __str__(self):
        return self.name
    

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="users/avatars/%Y/%m/&d",
        default='users/avatar/default/jpg'
    )
    bio=models.TextField(max_length=500, null=True)
    location=models.CharField(max_length=30, null=True)
    website=models.CharField(max_length=100,null=True)
    joined_date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = '2. Users'
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = '3. Categories'

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = '4. Tags'

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = RichTextField()
    featured_image = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    #each post can receive likes from multiple users, and each user can like multiple posts
    likes = models.ManyToManyField(User, related_name="post_like")

    #each post belong to one user and one category
    #each post has many tags and each tag has many posts
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = '5. Posts'

    def __str__(self):
        return self.title
    
    def get_number_of_likes(self):
        return self.likes.count()
    
class Comment(models.Model):
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    #each comment can receive likes from multiple users and each user can like many comments
    likes = models.ManyToManyField(User, related_name='liked_comments')


    #each comment belongs to one user and one post
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = '6. Comments'

    def __str__(self):
        if len(self.content) > 50:
            comment = self.content[:50] + '...'
        else:
            comment = self.content
        return comment
    
    def get_number_of_likes(self):
        return self.likes.count()
    
class UploadedFile(models.Model):
    file = models.FileField(upload_to='posts/featured_images/%Y/%m%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)