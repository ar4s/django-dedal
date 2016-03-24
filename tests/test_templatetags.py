from ddt import data, ddt, unpack

from django.test import TestCase

from dedal.templatetags.dedal_tags import crud

from example.blog.models import Post


@ddt
class CrudTemplatetagTest(TestCase):
    @unpack
    @data(
        ('list',),
        ('create',),
        ('read',),
        ('update',),
        ('delete',),
    )
    def test_crud_tag(self, action):
        post, _ = Post.objects.get_or_create(title='Foo', body='Lorem')
        self.assertTrue(crud(post, action))
