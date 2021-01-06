from django import forms
from .models import Movie, Comment_Score

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
class CommentScoreForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': '댓글을 작성하세요.'}))
    score = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': '평점을 작성하세요.'}))
    
    class Meta:
        model = Comment_Score
        fields = ['content', 'score']
        

    
         
    