from api import serializers
from api.models import Container, Plc
from rest_framework import viewsets
from rest_framework import permissions

# Allow an unauthenticated Post
# http://stackoverflow.com/questions/37642175/how-to-add-django-rest-framework-permissions-on-specific-method-only
class IsPostOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True

        # Otherwise, only allow authenticated requests
        return request.user and request.user.is_authenticated()

class ContainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for all containers
    """
    serializer_class = serializers.ContainerSerializer
    queryset = Container.objects.all()
    permission_classes = (IsPostOrIsAuthenticated,)
    filter_fields = ('status', 'ip_address')

class PlcViewSet(viewsets.ModelViewSet):
    """
    API endpoint for all plcs
    """
    serializer_class = serializers.PlcSerializer
    queryset = Plc.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('container_id','info1', 'info2')

