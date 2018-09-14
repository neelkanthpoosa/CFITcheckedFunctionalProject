from django.conf.urls import url
from forum import views
from forum.views import ForumView

app_name="forum"

urlpatterns=[
	url(r'^$',ForumView.as_view(),name='forum'),
	url(r'status/$',views.Status,name='status'),
]
