from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'code' , 'host' , 'guest_can_pause', 'votesToSkip', 'createdAt' )
