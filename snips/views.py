from snips.models import Snips
from snips.serializers import SnipsSerializer, UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView

from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnipsList(APIView):
    """
    List all snips, or create a new snips.
    """
    def get(self, request, format=None):
        snips = Snips.objects.all()
        serializer = SnipsSerializer(snips, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnipsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnipsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snips.objects.get(pk=pk)
        except Snips.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snips = self.get_object(pk)
        serializer = SnipsSerializer(snips)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snips = self.get_object(pk)
        serializer = SnipsSerializer(snips, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snips = self.get_object(pk)
        snips.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# from rest_framework import serializers
# from snips.permissions import IsOwnerOrReadOnly
# from django.http import HttpResponse, JsonResponse
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
# from rest_framework import permissions


# class SnipsList(generics.ListCreateAPIView):
#     queryset = Snips.objects.all()
#     serializer_class = SnipsSerializer
    
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class SnipsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snips.objects.all()
#     serializer_class = SnipsSerializer
    
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class UserSerializer(serializers.ModelSerializer):
#     snips = serializers.PrimaryKeyRelatedField(many=True, queryset=Snips.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snips']

# @api_view(['GET', 'POST'])
# def snips_list(request, format=None):
#     """
#     List all code snips, or create a new snips.
#     """
#     if request.method == 'GET':
#         snips = Snips.objects.all()
#         serializer = SnipsSerializer(snips, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnipsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def snips_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snips.
#     """
#     try:
#         snips = Snips.objects.get(pk=pk)
#     except Snips.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnipsSerializer(snips)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnipsSerializer(snips, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snips.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
