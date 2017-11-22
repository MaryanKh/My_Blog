from django.db import models

from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = models.TextField(max_length=10000) # текст поста

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/blog/%i/" % self.id
        return reverse('post-detail', args=[str(self.id)])


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class BlogComment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    content = models.TextField(max_length=1000, help_text="Enter comment about post here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring