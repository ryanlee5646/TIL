1. Class Based View와 URL을 연결해 주기 위해서는 Function Based View와는 다르게, urls.py에서 views를import 하고 해당 모듈에 있는 View Class들을 path함수로 넘겨주면서 특정 method를 호출하여 넘겨주어야한다. 아래 예시의(a)에 들어가야하는, 앞서 설명한 method를 작성하시오

`as_view()`



2. 

* ListView : 목록
* CreateView: 생성 
* DetailView: 상세
* UpdateView: 수정
* DeleteView: 삭제