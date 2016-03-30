# -*- coding: utf-8 -*-
from django.test import TestCase

from dedal import ACTIONS, ACTION_CREATE
from dedal.site import site, Dedal
from dedal.decorators import crud
from dedal.exceptions import ModelIsNotInRegisterError
from example.blog.models import Post


class FooModel(object):
    class _meta:  # noqa
        model_name = 'foo'


class TestDedalSiteRegistry(TestCase):
    def setUp(self):
        self.Model = crud(FooModel)

    def test_model_should_register_when_decorated(self):
        self.assertTrue(site.is_registered(self.Model))

    def test_model_should_unregister_when_registered(self):
        self.assertTrue(site.unregister(self.Model))
        self.assertFalse(site.is_registered(self.Model))

    def test_unregister_should_raise_error_when_not_in_register(self):
        site.unregister(self.Model)
        with self.assertRaises(ModelIsNotInRegisterError):
            site.unregister(self.Model)


class DedalObject(TestCase):
    def test_actions(self):
        actions = [ACTION_CREATE]
        instance = Dedal(site, Post, actions)
        for action in actions:
            self.assertTrue(hasattr(instance, action), action)

        for action in set(ACTIONS) - set(actions):
            self.assertFalse(hasattr(instance, action), action)
