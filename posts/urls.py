from django.conf.urls import url
from .views import posts_list, new_post, PostCreateView, post_detail, PostDetailView


urlpatterns = [
    url(r'^list/(?P<block_id>\d+)$', posts_list),
    url(r'^list/(?P<block_id>\d+)?page=(?P<page_no>)$', posts_list),
    url(r'^list/(?P<block_id>\d+)/new_post', new_post),
    # url(r'^list/(?P<block_id>\d+)/new_post$', PostCreateView.as_view()),
    url(r'^list/(?P<block_id>\d+)/post(?P<post_id>\d+)$', post_detail),
    url(r'^list/(?P<block_id>\d+)/post(?P<post_id>\d+)?page=(?P<page_no>)$', post_detail),
    # url(r'^list/(?P<block_id>\d+)/(?P<pk>\d+)$', PostDetailView.as_view()),
]
