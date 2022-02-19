from rest_framework import serializers
from snips.models import Snips, LANGUAGE_CHOICES, STYLE_CHOICES

class SnipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snips
        fields = ['id', 'bookname','bookauthor', 'booklan']
