from django.conf.urls.defaults import *

action_patterns = patterns('todo.views.actions',
    (r'^resolve/task/(?P<task_id>\d+)$', 'resolve_task'),
    (r'^resolve/step/(?P<step_id>\d+)$', 'resolve_step'),
)

api_patterns = patterns('todo.views.api',
    # move this to actions
    (r'^task/(?P<task_id>\d+)/update-snapshot$', 'update_snapshot'),
)

demo_patterns = patterns('todo.views.demo',
    (r'^task/(?P<task_id>\d+)$', 'task'),
    (r'^combined$', 'combined'),
    (r'^tracker/(?P<tracker_id>\d+)$', 'tracker'),
    (r'^trackers$', 'trackers'),
)

urlpatterns = patterns('',
    (r'new/$', 'todo.views.new'),
    (r'new/tasks$', 'todo.views.create', {'obj': 'tasks'},
     'todo-create-tasks'),
    (r'new/trackers$', 'todo.views.create', {'obj': 'trackers'},
     'todo-create-trackers'),
    # includes
    (r'^action/', include(action_patterns)),
    (r'^api/', include(api_patterns)),
    (r'^demo/', include(demo_patterns)),
)
