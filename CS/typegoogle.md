# what happens when you type google in the browser and press enter?

1. www.google.com을 브라우저 주소창에 친다.
2. Browser는 캐싱된 DNS 기록들을 통해 www.google.com에 대응되는 IP 주소가 있는지 확인한다.
   - DNS(도메인 네임 시스템(Domain Name System, **DNS**)은 호스트의 도메인 이름을 호스트의 네트워크 주소로 바꾸거나 그 반대의 변환을 수행할 수 있도록 하기 위해 개발되었다.)
   - DNS는 URL들의 이름과 IP 주소를 저장하고 있는 데이터베이스이다.
   - 인터넷의 모든 URL들에는 고유의 IP 주소가 지정되어 있다. 이 IP 주소를 통해서 해당 웹사이트를 호스팅하고있는 서버 컴퓨터에 접속할 수 있다. 
   - DNS는 전화번호부와 비슷한 역할을 한다. 
   - DNS의 가장 큰 목적은 사람들에게 편리함을 주기 위해서다. 숫자로된 IP 주소를 작성해도 원하는 웹사이트에 접속할 수 있지만 랜덤한 숫자들을 검색하는 것은 복잡하다. 
   - 웹 사이트 이름을 브라우저에 검색하면 브라우저는 DNS 기록을 4가지의 캐시에서 확인한다.
     - 첫번째로. 브라우저 캐시 확인(유저가 이전에 설정한 DNS 기록들 저장하고 있다. DNS query가 가장 먼저 실행)
     - 찾지 못했다면, OS 캐시 확인(브라우저는 systemcall을 통해서 OS가 저장하고 있는 DNS 기록들의 캐시에 접근)
     - 찾지 못했다면. router 캐시 확인(DNS 기록을 캐싱하고 있는 router와 통신을 해서 찾으려고 한다.)
     - 찾지 못했다면 ISP 캐시 확인(ISP는 DNS서버를 구축하고 있고 브라우저가 마지막으로 DNS기록이 있기를 바라며 접근하게 된다.)
   - 캐시는 네트워크 트래픽을 조절하고 데이터 전송 시간을 줄이기 위해 매우 중요하다.
3. 요청한 URL이 캐시가 없으면 ISP의 DNS 서버가 www.google.com을 호스팅하고 있는 서버의 IP 주소를 찾기 위해 DNS query를 날린다. 
   - www.google.com에 접속하고 싶으면 IP주소를 반드시 알아야한다.
   - DNS query의 목적은 여러 다른 DNS 서버들을 검색해서 해당 사이트의 IP 주소를 찾는것이다. -> `recursive search` 라고 부른다. 
   - IP 주소를 찾을 때까지 DNS 서버에서 다른 DNS 서버를 오가면서 반복적으로 검색하던지 못 찾아서 에러가 발생할 때 까지 검색을 진행한다.
   - 이 상황에서, ISP의 DNS 서버를 DNS recursor라고 부르고 인터넷을 통해 다른 DNS 서버들에게 물어 물어 도메인 이름의 올바른 IP 주소를 찾는데 책임을 갖고 있다. 다른 DNS 서버들은 name server라고 불린다. 이들은 웹사이트 도메인 이름의 구조에 기반해서 검색을 하기때문이다.
   - ![browser work dns 2](https://devjin-blog.com/static/df40acaf929fb371a270155e2ef49a36/fcda8/browser_work_dns_2.png)

4. Browser가 서버와 TCP connection을 한다. 
5. Browser가 웹 서버에 HTTP 요청을 한다.
6. 서버가 요청을 처리하고 response를 생성한다.
7. 서버가 HTTP response를 보낸다. 
8. Browser가 HTML content를 보여준다. 