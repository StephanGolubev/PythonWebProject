from django.urls import include, path
from . import views
from blog.feeds import LatestPostsFeed


app_name = 'blog'

urlpatterns = (
    path('', views.post_list, name='pots_list'),
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('about_me', views.about_me, name='about_me'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
)
