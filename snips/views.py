from snips.models import Snips
from snips.permissions import IsOwnerOrReadOnly
from snips.serializers import SnipsSerializer, UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework import permissions

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnipsList(generics.ListCreateAPIView):
    queryset = Snips.objects.all()
    serializer_class = SnipsSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnipsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snips.objects.all()
    serializer_class = SnipsSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserSerializer(serializers.ModelSerializer):
    snips = serializers.PrimaryKeyRelatedField(many=True, queryset=Snips.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snips']

@api_view(['GET', 'POST'])
def snips_list(request, format=None):
    """
    List all code snips, or create a new snips.
    """
    if request.method == 'GET':
        snips = Snips.objects.all()
        serializer = SnipsSerializer(snips, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnipsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snips_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snips.
    """
    try:
        snips = Snips.objects.get(pk=pk)
    except Snips.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnipsSerializer(snips)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnipsSerializer(snips, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snips.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

