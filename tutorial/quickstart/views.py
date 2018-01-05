from django.contrib.auth.models import User, Group
from .models import Champion, Item
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, ChampionSerializer, ItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ChampionViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Item.objects.all()
    serializer_class = ItemSerializer