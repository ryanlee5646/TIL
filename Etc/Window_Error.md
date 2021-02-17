## Windows 에러



### 1. 윈도우에러(0xc0150004)

<img src = "./images/error1.PNG" width="100%">

1. **cmd**창 관리자 권한으로 실행
2. `DISM.exe /Oline /Cleanup-image /Restorehealth` 명령어 실행

<img src = "./images/error2.PNG" width="100%">

3. SFC 무결성 검사

   `sfc /scannow` 실행