from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from rest_framework.authtoken.models import Token


# https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
# these are the database fields
class Container(models.Model):
    container_id = models.CharField(max_length=128, unique=True, primary_key=True)
    ip_address = models.GenericIPAddressField(protocol='IPv4', unpack_ipv4=False)
    passwd_hash = models.CharField(max_length=128, null=True)
    status = models.IntegerField(null=True)
    timestamp = models.TimeField(auto_now=True, auto_now_add=False)
    
    #def update(self):
    #    self.timestamp = models.TimeField(auto_now=True)
    #    #self.save(update_fields=['timestamp'])
    #    #self.save(force_update=True)
    #    #self.save(update_fields=True)
    #    self.save()
        
    def update(self):
        print "models function"
        container = self.container_id
        container.save()


