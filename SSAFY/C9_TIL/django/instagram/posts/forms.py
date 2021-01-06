from django import forms
from .models import Post, Comment, Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # models.py 에 지정된 클래스 명
        fields = ['content',] # Post테이블에 image항목을 다른데로 옮겼으므로  'image' 항목을 삭제
        

        
class ImageForm(forms.ModelForm): # Post 등록하는 페이지에 글쓰는 form과 파일(이미지)을 등록하는 form을 따로 하나 더 만듬.
    class Meta:
        model = Image
        fields = ['file',]
        
ImageFormSet = forms.inlineformset_factory(Post, Image, form=ImageForm, extra=3) # 이미지 Form들을 엮은 FormSet을 만듬
#첫번째 인자값: 이미지를 들고있는(부모) 모델, 두번째 인자값: 레코드를 생성할 형태, 세번째: 이미지를 만들 form의 종류, 네번째: 만들 form의 최대개수) 
class CommentForm(forms.ModelForm): #view.py에 list함수에다가 씀
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'댓글을 작성하세요.'}))
    # 원래 Textfield로 되어 있던 것을 Charfield로 변경, content라는 라벨도 빈 라벨로 변경
    # models.py에서 기본형식은 텍스트필드라서 글자수 제한이 없고 글쓰는 칸의 형태만 CharField로만 변경
    class Meta:
        model = Comment
        fields = ['content',]
        
# OpereationalError at [URL]
# no such column: movies_score.movie_id