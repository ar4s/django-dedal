from django import template
from django.core.urlresolvers import reverse

from dedal import ACTIONS_REQUIRED_OBJ

register = template.Library()


@register.simple_tag
def crud(obj, action):
    obj_name = obj._meta.model_name
    args = []
    if action in ACTIONS_REQUIRED_OBJ:
        args = [obj.pk]
    return reverse('{}:{}'.format(obj_name, action), args=args)


register.filter(
    'verbose_name_plural', lambda x: x._meta.verbose_name_plural
)

register.filter(
    'repr', lambda x: repr(x)
)
