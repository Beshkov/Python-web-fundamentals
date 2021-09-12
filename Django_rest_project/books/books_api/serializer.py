from rest_framework import serializers
from .models import BookModel

class BookSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        title = attrs['title']
        if title:
            star_letter = title[0]
            if star_letter.islower():
                raise serializers.ValidationError('Must start with capital letters')
        return attrs


    class Meta:
        model = BookModel
        fields = "__all__"
