from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="events:user-detail")

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name')
