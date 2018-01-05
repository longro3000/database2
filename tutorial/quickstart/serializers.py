from django.contrib.auth.models import User, Group
from .models import Champion, Item
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ChampionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Champion
        fields = ('url', 'name', 'skills', 'story')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('url', 'name', 'price', 'passive')