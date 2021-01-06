1. **DOM에서 특정 요소를 선택할 때 `document.querySelector()` 뿐만 아니라 `document.querySelectorAll()` 역시 사용할 수 있다. 둘의 차이를 검색하여 기술하시오.**

    * `document.querySelector()` : 같은 태그 혹은 클래스 중 첫번째 element를 반환, 없으면 Null

    * `document.querySelectorAll():`: 해당 태그 혹은 클래스를 모두 찾아줌, 찾은 요소들이 배열됨, 없으면 빈 배열

      

2. **JS에서 자주 사용하는 EventListener 들 중 아래와 같은 것들이 있다. 각각 간략하게 어떤 Trigger 를 의미하는지 조사하여 간략하게 기술하시오.**

   http://www.ktword.co.kr/abbr_view.php?m_temp1=2744

   * mouse 이벤트

     * **click**: 마우스 버튼 클릭하고 버튼에서 손을 뗌(떼는 순간 발생하는 이벤트)
     * **mouseover**: 마우스 포인터가 요소 위에 올라감
     * **mouseout**: 마우스 포인터가 요소 밖으로 벗어남
     * **mousemove**: 마우스 포인터가 움직임

   * keyboard 이벤트

     * **keypress**: 키를 눌러 문자가 연결되었을 때
     * **keydown**: 키를 누르는 순간
     * **keyup**: 키를 눌렀다 떼는 순간

   *  문서(document)/ 창(window) 이벤트

     * **load**: HTML 문서 및 추가 자원(이미지 등)들을 모두 불러왔을 때 발생
     * **scroll**: 스크롤바를 드래그하거나 또는 키보드(위/아래/home/end 등) 또는 마우스휠 사용

   * 폼 이벤트

     * **change**: 폼 필드에서 변경이 일어남 (텍스트 변동,라디오 버튼의 클릭 등)

     

3. **DOM 에 요소를 추가할 때, innerHTML += 의 방법과 appendChild() 함수를 통해 추가하는 방법이 있다. 둘의 차이를 간략하게 기술하시오.**

   - innerHTML +=  :  전체 태그에 합쳐지는 효과
     		  전체데이터 + 추가데이터 새로 쓰는 효과

   ```html
   변수.innerHTML += '<h1>Hi</h1>' # 기존에 있는 거에다가 추가
   ```

   

   - appendChild()   : 선택된 태그 안, 제일 마지막 자식으로  element 를 추가
         ≒  `childNodes` 컬렉션의 제일 뒤에 첨부한다 

     ​							  추가데이터만 새로 쓰는 효과