import functools

from dedal.site import site


def register(model=None, actions=['create', 'read', 'update', 'delete']):
    if not model:
        return functools.partial(register, actions=actions)
    site.register(model, actions)

crud = register
