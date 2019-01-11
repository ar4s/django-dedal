import sys
from ddt import data, ddt, unpack
from django.conf import settings
from imp import reload
from importlib import import_module

from django.test import TestCase

from dedal import ACTIONS, ACTION_CREATE, ACTIONS_REQUIRED_OBJ
from dedal.compat import clear_url_caches, reverse, NoReverseMatch
from dedal.decorators import crud
from example.blog.models import Post


class FooModel(object):
    class _meta:  # noqa
        model_name = 'foo'


def reload_urlconf():
    clear_url_caches()
    if settings.ROOT_URLCONF in sys.modules:
        reload(sys.modules[settings.ROOT_URLCONF])
    return import_module(settings.ROOT_URLCONF)


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


@ddt
class TestActionsViews(TestCase):
    @classmethod
    def tearDownClass(cls):
        crud(Post)
        reload_urlconf()

    @unpack
    @data(
        ([ACTION_CREATE],),
    )
    def test_specified_actions(self, actions):
        post = Post.objects.create(title='test', body='test')
        crud(Post, actions)
        for action in ACTIONS:
            reload_urlconf()
            args = ()
            if action in ACTIONS_REQUIRED_OBJ:
                args = (post.pk,)
            if action in actions:
                response = self.client.get(
                    reverse('post:{}'.format(action), args=args)
                )
                self.assertEqual(response.status_code, 200)
            else:
                with self.assertRaises(NoReverseMatch):
                    reverse('post:{}'.format(action), args=args)
