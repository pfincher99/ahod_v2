from rest_framework import serializers
from api.models import Container

class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Container
        fields = ('container_id', 'ip_address', 'passwd_hash', 'status', 'timestamp')
