import django

if django.VERSION >= (2, 0):
    from django.urls import clear_url_caches, reverse, NoReverseMatch
else:
    from django.core.urlresolvers import clear_url_caches, reverse, NoReverseMatch
