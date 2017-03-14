from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views as restviews
from api.views import HeartbeatViewset
from api.views import RegisterViewset

router = routers.DefaultRouter()
router.register(r'register',
                RegisterViewset,
                base_name='container-detail')

# router.register(r'heartbeat',
#                HeartbeatViewset,
#                base_name='register-detail')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/container/(?P<container_id>.+)/$',HeartbeatViewset.as_view()),
    url(r'^api/v1/container/', include(router.urls)),
    url(r'^api/v1/auth/', restviews.obtain_auth_token),
]
