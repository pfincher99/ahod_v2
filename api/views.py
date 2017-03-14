from django.shortcuts import render
from api import serializers
from api.models import Container
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

class ContainerViewSet(viewsets.ModelViewSet):

    """
    API endpoint for all containers
    """
    serializer_class = serializers.ContainerSerializer
    queryset = Container.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('status', 'ip_address')

## Original class
# class RegisterViewset(viewsets.ModelViewSet):
#
#     """
#     API endpoint for all endpoints
#     """
#     serializer_class = serializers.ContainerSerializer
#     queryset = Container.objects.all()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     #def perform_create(self, serializer):
#     #    serializer.save()
#
#
# class HeartbeatViewset(viewsets.ModelViewSet):
#
#     """
#     API endpoint for endpoints with status =1
#     """
#     serializer_class = serializers.ContainerSerializer
#     queryset = Container.objects.filter(status=1)
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
