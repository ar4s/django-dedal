import functools

from dedal import ACTIONS
from dedal.site import site


def register(model=None, actions=ACTIONS):
    if not model:
        return functools.partial(register, actions=actions)
    site.register(model, actions)
    return model

crud = register
