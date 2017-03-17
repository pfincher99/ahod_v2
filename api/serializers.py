from rest_framework import serializers
from api.models import Container, Plc

class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Container
        #fields = ('container_id', 'ip_address', 'passwd_hash', 'status', 'timestamp')
        fields = ('container_id', 'ip_address','timestamp')


class PlcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plc
        fields = ('container_id','info1', 'info2')
