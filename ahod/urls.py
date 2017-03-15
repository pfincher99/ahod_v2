from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views as restviews
from api.views import ContainerViewSet, PlcViewSet

router = routers.DefaultRouter()
router.register(r'container',
                ContainerViewSet,
                base_name='container'
                )
router.register(r'plc',
                PlcViewSet,
                base_name='plc'
                )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/', restviews.obtain_auth_token),
    url(r'^api/v1/', include(router.urls)),
]
