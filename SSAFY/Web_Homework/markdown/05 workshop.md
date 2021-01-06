- Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다. 따라서, 단어를 입력받아 Palindrome을 검증하고True나 False를 리턴하는 함수palindrome(word)를 만들어 보세요.

```python
   def is_palindrom(word):
        return word == word[::-1] #s[start:end:step]
```

```python
def is_palindrom(word):
    list_word = list(word) # ['l','e','v','e','l']
    for i in range(len(list_word)//2):
        if list_word[i] != list_word[-i-1]:
            return False
    return True
```

