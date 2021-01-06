from urllib.parse import urljoin

baseUrl = "https://test.com/html/a.html"
print(">>", urljoin(baseUrl, "b.html"))
print(">>", urljoin(baseUrl, "sub/b.html"))
print(">>", urljoin(baseUrl, "../index.html"))
print(">>", urljoin(baseUrl, "../img/img.jpg"))
print(">>", urljoin(baseUrl, "../css/img.css"))
# urljoin을 사용하게 되면 절대 경로는 묶어놓고 나머지 파일의 위치만 조정 가능
# ..을 사용하게 되면 한칸 윗단계로 올라감, 위에 올라 갔을때 절대 경로위치면 그 위치부터 경로 설정
