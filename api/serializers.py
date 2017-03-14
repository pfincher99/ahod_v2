from rest_framework import serializers
from api.models import Container

class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.IntegerField()

    class Meta:
        model = Container
        fields = ('container_id', 'ip_address', 'passwd_hash', 'status', 'timestamp')
       
   

#class DatapointSerializer(serializers.HyperlinkedModelSerializer):
#    device = DeviceSerializer()
#
#    class Meta:
#        model = Datapoint
#        fields = ('device', 'monitor','devicetype')
#
#    def create(self, validated_data):
#        device = validated_data.pop('device')
#        print device
#        device = Device.objects.get_or_create(name=device['name'], note=device['name'])[0]
#        dp = Datapoint.objects.create(device=device, **validated_data)
#        return dp