ACTIONS = ('create', 'read', 'update', 'delete', 'list')
ACTION_CREATE, ACTION_READ, ACTION_UPDATE, ACTION_DELETE, ACTION_LIST = ACTIONS
ACTIONS_REQUIRED_OBJ = set((ACTION_READ, ACTION_UPDATE, ACTION_DELETE))
ACTIONS_RE = {
    ACTION_LIST: r'^list$',
    ACTION_CREATE: r'^{}/$'.format(ACTION_CREATE),
    ACTION_READ: r'^(?P<pk>\d+)/$',
    ACTION_UPDATE: r'^(?P<pk>\d+)/{}/$'.format(ACTION_UPDATE),
    ACTION_DELETE: r'^(?P<pk>\d+)/{}/$'.format(ACTION_DELETE),
}
