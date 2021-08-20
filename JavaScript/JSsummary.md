# JS summary

실행 컨텍스트

```jsx
처음 코드 실행
-> 전역 컨텍스트 생성(모든 것 관리하는 환경, 페이지 종료될때까지 유지)
-> 함수 호출할 때마다 함수 컨텍스트 생성
-> 컨텍스트 생성시 컨텍스트 안에 변수객체, 스코프 체인, this 생성
-> 컨텍스트 생성 후 함수가 실행 -> 사용되는 변수들은 변수 객체안에서 값을 찾고,
																없으면 스코프 체인을 따라 올라가며 찾는다.
-> 함수 실행 마무리되면 해당 컨텍스트는 사라짐(클로저 제외)
-> 페이지 종료(전역 컨텍스트 사라짐)
```

클로저

```jsx
내부함수가 외부함수의 지역변수에 접근할 수 있는 것!
외부함수는 외부함수의 지역변수를 사용하는 내부함수가 소멸될때까지 소멸되지 않는다.
비공개 변수 : 남들이 조작하지 못한다.
단점 : 성능 문제, 메모리 문제, 스코프 체인을 거슬러 올라가는 행동 -> 느려짐
```

this

```jsx
1. 객체안에 메소드
2. 프로토타입 객체안의 메소드
3. 생성자 함수
4. apply call bind
```

스코프, 스코프체인

```jsx
스코프 체인 : 스코프가 계층적으로 연결된 것
- 실행 컨텍스트의 렉시컬 환경을 단방향으로 연결한 것
- 변수 참조할 때 : 자바스크립트 엔진은 스코프 체인을 통해 변수를 참조하는
									스코프에서 시작하여 상위 스코프로 이동하여 검색
함수레벨 스코프 : 코드 블록이 아닌 함수에 의해서만 지역 스코프가 생성 
- var 키워드로 선언된 변수는 함수의 코드블록만을 지역 스코프로 인정한다.
블록레벨 키워드 : let, const
렉시컬 스코프(정적 스코프, Javascript) : 함수를 어디서 정의했는지에 따라 함수의 상위 스코프 결정
- 함수 정의가 실행될 때 정적으로 결정된다.
- 함수는 선언할 때 스코프가 생성됨
동적 스코프 : 함수를 어디서 호출했는지에 따라 함수의 상위 스코프 결정
```

이벤트 루프

```jsx
코드 블럭안에서 또 다른 코드블럭을 만들거나
이벤트 리스너를 등록하는 함수를 만들때
렉시컬 스코프
그 위에 정의된 변수들의 데이터가 다 함께 저장되어져서 전달이 됩니다.
```

버블링캡쳐링

```jsx
- 부모에서부터 내려와서 event handler 호출(capturing)
- 자식의 이벤트가 호출되면 부모에게도 이벤트 호출 (bubbling)
event.stopPropagation() 
event.target, event.currentTarget
```

프로미스

```jsx
객체
const promise = new Promise((resolve, reject) => {
  try {
    ...비동기 작업
    resolve(결과);
  } catch (err) {
    reject(err);
  }
});
resolve는 성공했을 때 결과, reject는 실패했을 때 에러
promise.then((result) => {
  // result 처리
}).catch((err) => {
  console.error(err);
});
resolve(결과)의 결과가 then의 result
reject(err)의 err이 catch의 err
then과 catch로 결과를 받는다.
Users.findOne({}).then((user) => {
  user.name = 'zero';
  return user.save();
}).then((user) => {
  return Users.findOne({ gender: 'm' });
}).then((user) => {
  ...
}).catch(err => {
  console.error(err);
});
장점
1. 코드 분리 가능
2. 조건문별로 따로 처리 가능, 변수에 대입할 수 있어서 활용도 높음
3. then을 여러번 연속해서 쓸 수 있다.
단점
1. 마지막 catch에서 에러를 한 번에 처리하기 때문에 어디서 에러 났는지 확인하기 어려움
-> 해결 방법 : return 하는 Promise 객체에 catch 붙인다. 
							throw로 에러를 발생시키면 뒤의 then이 호출되지 않고 catch로 넘어간다.
```

async await

```jsx
await이 Promise 객체를 받아 처리하는 키워드
async함수는 Promise가 없으면 의미 없다.
async 함수는 return 또는 throw 값이 담긴 Promise를 리턴한다.
await은 반드시 async 함수 바로 안에서만 쓰여야한다.
에러 처리 -> try catch 문으로 감싼다.
```

mobx, redux, context API

```jsx
Redux : 하나의 store에 하나의 object로 관리 
				action의 type을 기준으로 action 분류, 
				action에 따라 state 변경
MobX : 데코러이터로 가독성있고 쉽게 코드를 짤 수 있게 
			 클래스형 컴포넌트 기준으로 맞춰져 있음
Context : React Components에서만 작동, context값이 변경되면 전체 리렌더링
					store또는 관리하는 것이 없음
					많은 컴포넌트에 리렌더링을 많이 해도 상관없을때
```

SWR

```jsx
원격서버의 상태를 가져와서 리액트 컴포넌트에 꽂아주는 기능
useSWR은 한번 fetch한 원격상태의 데이터를 내부적으로 캐시하고
다른 컴포넌트에서 동일한 상태를 사용하고자 할 경우
이전 캐시했던 상태 그대로 리턴해준다.
컴포넌트간 전역 상태를 공유할 수 있다.
```

html css javascript가 브라우저에서 어떻게 렌더링 되는지

```jsx
requests/response 
→ loading 
→ scripting
(HTML 한줄씩 읽기 (태그를 분석해서 Node로 변환)-> DOM(Document Object Model),
 CSS -> CSSOM)
→ rendering(렌더트리 만든다) 
→ layout(요소들 위치, 크기 계산) 
→ painting(요소들의 배치에 따라 각각 부분을 잘게 나눠서 이미지를 준비, 레이어) 
-> composition (레이어들을 브라우저에 순서대로 올려놓습니다)

layout, painting을 자주 해야하는 일이 일어나면 효율성이 좋지 않습니다. 
DOM 트리 구축위한 HTML 파싱 
-> 렌더트리 구축
-> 렌더트리 배치
-> 렌더트리 그리기
```

BOM

```jsx
웹 브라우저의 창이나 프레임을 추상화해서 
프로그래밍적으로 제어할 수 있도록 제공하는 수단
```

DOM

```jsx
HTML파일 브라우저에 읽기
-> 태그 분석해서 Node로 변환
-> Node는 EventTarget 상속받습니다.
-> DOM 트리로 변환 (HTML 태그에는 그에 상응하는 DOM Tree 요소가 있다.)
가상 요소 포함하지 않음(ex. ::after)
보이지 않는 요소 포함(ex. display:none)
```

CSSOM

```jsx
정의한 스타일
브라우저에 기본적으로 설정된 속성값 등
모든 CSS 값들이 정의되어져 있음
```

Render Tree

```jsx
DOM 과 CSSOM이 합쳐져서 Render Tree가 만들어집니다.
Render Tree에는 사용자에게 궁극적으로 보여지는 아이들만 선별
- opacity:0, visibility: hidden -> render tree에 들어감
- display: none -> render tree에 안들어감
```