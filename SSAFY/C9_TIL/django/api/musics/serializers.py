from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist',]
        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name',]
        
class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True) # music_set(music에 대한 정보를 serialize시켜줌)
    class Meta:
        model = Artist
        fields = ['id','name','music_set',] 
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content',]