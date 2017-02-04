from django.conf.urls import url

from task.views import TaskListView, TaskView
#from task.views import JSONResponse


helper_patterns = [
    #url(r'^tasks/$', JSONResponse.snippet_list ),
	#url(r'^task/(?P<pk>[0-9]+)/$', JSONResponse.snippet_detail),

	url(r'^tasks/$', TaskListView.as_view(), name='tasks'),
	url(r'^task/(?P<pk>[0-9]+)/$', TaskView.as_view(), name='get_task'),
]

urlpatterns = helper_patterns