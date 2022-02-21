from rest_framework import serializers
# from snips.models import Snips, LANGUAGE_CHOICES, STYLE_CHOICES
from snips.models import Snips
from django.contrib.auth.models import User

# owner = serializers.ReadOnlyField(source='owner.username')

class SnipsSerializer(serializers.ModelSerializer):
    # snips = serializers.PrimaryKeyRelatedField(many=True, queryset=Snips.objects.all())
    class Meta:
        model = Snips
        fields = ['id', 'bookname','bookauthor', 'booklan']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']