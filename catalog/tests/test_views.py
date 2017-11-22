from django.test import TestCase

# Create your tests here.


from catalog.models import Post, Author
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User  # Blog author or commenter


class BlogListView(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        blog_author = Author.objects.create(user=test_user1, content='This is a content')

        number_of_blogs = 13
        for blog_num in range(number_of_blogs):
            Post.objects.create(name='Test Blog %s' % blog_num, author=blog_author,
                                content='Test Blog %s Description' % blog_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/post/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('post'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('post'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'catalog/blog_list.html')

    def test_pagination_is_five(self):
        resp = self.client.get(reverse('post'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertEqual(len(resp.context['blog_list']), 5)