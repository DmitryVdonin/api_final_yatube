from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'api'

router_v1 = routers.SimpleRouter()
router_v1.register(r'v1/posts', views.PostViewSet)
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments', views.CommentViewSet,
    basename='comment',
)
router_v1.register(r'v1/groups', views.GroupViewSet)
router_v1.register(r'v1/follow', views.FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router_v1.urls)),
]
