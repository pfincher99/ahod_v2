from api import serializers
from api.models import Container
from rest_framework import viewsets
from rest_framework import permissions

class ContainerViewSet(viewsets.ModelViewSet):

    """
    API endpoint for all containers
    """
    serializer_class = serializers.ContainerSerializer
    queryset = Container.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('status', 'ip_address')


