from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'v1/posts', views.PostViewSet)
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments', views.CommentViewSet,
    basename='comment',
)
router.register(r'v1/groups', views.GroupViewSet)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
    path('v1/follow/', views.FollowList.as_view()),
]
