from api import serializers
from api.models import Container, Plc
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

class PlcViewSet(viewsets.ModelViewSet):

    """
    API endpoint for all containers
    """
    serializer_class = serializers.PlcSerializer
    queryset = Plc.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #filter_fields = ('info1', 'info2')
