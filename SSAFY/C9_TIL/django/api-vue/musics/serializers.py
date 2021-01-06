from rest_framework import serializers
from .models import Music, Artist, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content',]

class MusicSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name')
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist_name', 'comment_set',] # 'comment_set' 이 음악이 들고있는 댓글들을 같이 보여줌
        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name',]
        
class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True) # music_set(music에 대한 정보를 serialize시켜줌)
    class Meta:
        model = Artist
        fields = ['id','name','music_set',] 
        
