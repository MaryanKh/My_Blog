from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User  # Blog author or commenter
from catalog.models import Author, Post, BlogComment


class BlogAuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        Author.objects.create(user=test_user1, content='This is a bio')

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')

    def test_user_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_bio_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

    def test_bio_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('content').max_length
        self.assertEquals(max_length, 400)

    def test_object_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = author.user.username
        self.assertEquals(expected_object_name, str(author))


import datetime


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        blog_author = Author.objects.create(user=test_user1, bio='This is a content')
        blog = Post.objects.create(name='Test Blog 1', author=blog_author, content='Test Blog 1 Description')

    def test_get_absolute_url(self):
        blog = Post.objects.get(id=1)
        self.assertEquals(blog.get_absolute_url(), '/blog/blog/1')

    def test_name_label(self):
        blog = Post.objects.get(id=1)
        field_label = blog._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        blog = Post.objects.get(id=1)
        max_length = blog._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_description_label(self):
        blog = Post.objects.get(id=1)
        field_label = blog._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

    def test_description_max_length(self):
        blog = Post.objects.get(id=1)
        max_length = blog._meta.get_field('content').max_length
        self.assertEquals(max_length, 2000)

    def test_date_label(self):
        blog = Post.objects.get(id=1)
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label, 'post date')

    def test_date(self):
        blog = Post.objects.get(id=1)
        the_date = blog.post_date
        self.assertEquals(the_date, datetime.date.today())

    def test_object_name(self):
        blog = Post.objects.get(id=1)
        expected_object_name = blog.name
        self.assertEquals(expected_object_name, str(blog))


class BlogCommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()
        blog_author = Author.objects.create(user=test_user1, content='This is a bio')
        blog_test = Post.objects.create(name='Test Blog 1', author=blog_author, content='Test Blog 1 Description')
        blog_comment = BlogComment.objects.create(content='Test Blog 1 Comment 1 Description', user=test_user2,
                                                  post=blog_test)

    def test_description_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

    def test_description_max_length(self):
        blogcomment = BlogComment.objects.get(id=1)
        max_length = blogcomment._meta.get_field('content').max_length
        self.assertEquals(max_length, 1000)

    def test_author_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_date_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label, 'post date')

    def test_blog_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('post').verbose_name
        self.assertEquals(field_label, 'post')

    def test_object_name(self):
        blogcomment = BlogComment.objects.get(id=1)
        expected_object_name = ''
        len_title = 75
        if len(blogcomment.description) > len_title:
            expected_object_name = blogcomment.description[:len_title] + '...'
        else:
            expected_object_name = blogcomment.description

        self.assertEquals(expected_object_name, str(blogcomment))