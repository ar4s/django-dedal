from django import template

from dedal import ACTIONS_REQUIRED_OBJ
from dedal.compat import reverse
from dedal.site import site

register = template.Library()


@register.simple_tag
def crud(obj, action):
    obj_name = obj._meta.model_name
    args = []
    if action not in site.get_actions(obj.__class__):
        return '#not_found'
    if action in ACTIONS_REQUIRED_OBJ:
        args = [obj.pk]
    return reverse('{}:{}'.format(obj_name, action), args=args)


register.filter(
    'verbose_name_plural', lambda x: x._meta.verbose_name_plural
)

register.filter(
    'repr', lambda x: repr(x)
)
