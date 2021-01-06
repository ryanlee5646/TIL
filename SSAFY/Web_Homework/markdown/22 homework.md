1. **attachment column에 파일을 저장하려고 한다. 아래의(a)에 정의해야하는 field는?**

`model.FileField()`

2. **사용자가 업로드 한 파일이 저장되는 위치를 Django 프로젝트폴더 내부의'/uploaded_files'로 지정하고자 한다. 이때, settings.py에 작성해야 할 설정 2가지와 이것이 의미하는 바를 간략하게 작성하시오.**

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')
```

3. **개발자가 작성한CSS 파일이나 넣고자하는 이미지파일 등이 Django 프로젝트 폴더 내부의 '/assets'에 있다. '이 폴더 안에 정적파일이 있다.'라고 Django 프로젝트에게 알려주기위해서 settings.py에 작성해야하는 설정을 작성하시오.**

```python
STATICFILES_DIR = {
    os.path.join(BASE_DIR, 'assets'),
}
```





