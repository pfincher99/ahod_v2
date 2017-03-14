from django.shortcuts import render
from api import serializers
from api.models import Container
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

## Original class
class RegisterViewset(viewsets.ModelViewSet):

    """
    API endpoint for all endpoints
    """
    serializer_class = serializers.ContainerSerializer
    queryset = Container.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    #def perform_create(self, serializer):
    #    serializer.save()

    
class HeartbeatViewset(generics.RetrieveUpdateAPIView):

    """
    API endpoint for endpoints with status =1
    """
    serializer_class = serializers.ContainerSerializer
    queryset = Container.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = "container_id"
    lookup_url_kwarg = 'container_id'
    
    def update(self, request, *args, **kwargs):
        serializer = serializers.ContainerSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            # do some magic here
            return Response(serializer.data, status=status.HTTP_200_OK)
