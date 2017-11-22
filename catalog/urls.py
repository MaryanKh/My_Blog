from django.conf.urls import url

from. import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.PostListView.as_view(), name='posts'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.BlogCommentCreate.as_view(), name='blog_comment'),
]
