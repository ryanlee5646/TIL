from django.shortcuts import render, get_object_or_404
from .models import Music, Artist, Comment
from rest_framework.decorators import api_view
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer
from rest_framework.response import Response


@api_view(['GET']) # 들어오는 특정한 http메서드가 어떤 요청인지 대한 필터링
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True) # 여기에는 Music이 많이 들었다는 정보를 알려줘야함
    return Response(serializer.data)
    # Serialize: 들어오 많은 데이터들 중 
    # 필요한 데이터를 뽑아와서 한줄 문자열로 나열하게 하는 행위
    # 기존에는 render나 redirect를 통해 다른곳으로 요청을 보내주는 메서드를 썻으나
    # Response는 페이지를 만들어서 이쁘게 정리한 걸 응답을 해줌
   
@api_view(['GET'])    
def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    serializer = MusicSerializer(music)
    return Response(serializer.data)
    
@api_view(['GET'])     
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
   
@api_view(['GET'])      
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['POST']) # 댓글을 생성하는 요청이기 때문에 POST
def comment_create(request, music_id):
    serializer = CommentSerializer(data=request.data) 
    # 원래 request.POST로 넘겨주나 serrialize는 data를 넘겨줘야함
    if serializer.is_valid(raise_exception=True): # 잘못된 요청이 들어왔을때 실제로 잘못됐다고 알려줌 raise_exception=True
        serializer.save(music_id=music_id)
        return Response(serializer.data)
        
@api_view(['PUT','DELETE']) # 댓글을 생성하는 요청이기 때문에 POST
def comment_update_and_delete(request, music_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Comment has been updated!'})
    else: 
        comment.delete()
        return Response({'message': 'Comment has been deleted!'})