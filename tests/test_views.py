from ddt import data, ddt, unpack

from django.core.urlresolvers import reverse
from django.test import TestCase

from example.blog.models import Post


@ddt
class TestBlogViews(TestCase):
    @unpack
    @data(
        ('post:list', 200, False),
        ('post:read', 404),
        ('post:create', 200, False),
        ('post:update', 404),
        ('post:delete', 404),
    )
    def test_urls(self, name, code, args=True):
        args = (0,) if args else ()
        url = reverse(name, args=args)
        response = self.client.get(url)
        self.assertEqual(response.status_code, code)

    def test_list_view(self):
        url = reverse('post:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_view(self):
        expected = 'Lorem ipsum'
        post = Post.objects.create(title='test', body='body test')
        url = reverse('post:update', args=(post.pk,))
        self.client.post(url, {'title': expected, 'body': expected})
        post = Post.objects.get(pk=post.pk)
        self.assertEqual(expected, post.title)
        self.assertEqual(expected, post.body)

    def test_create_view(self):
        expected = 'Lorem ipsum'
        url = reverse('post:create')
        self.client.post(url, {'title': expected, 'body': expected})
