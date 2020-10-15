# Javascript: Asynchronous Programming



Web API 

**DOM 접근 가능**

[https://developer.mozilla.org/ko/docs/Web/API](https://developer.mozilla.org/ko/docs/Web/API)

## Asynchronous Programming

동기 프로그래밍은 여러개의 작업이 있을 때 한 작업이 끝나기까지 기다렸다가 끝나면 다른 작업을 진행하는 방식이다. 비동기 프로그래밍은 한 작업이 완료되기 전에 다른 작업을 진행하는 방식이다. 

Web API ❤️ Asynchronous

Callback : 아주 오래된 비동기 방식

### **Promise**

**비동기식 작업의 처리를 위한 객체 (ES6에서 처음 소개)**

```jsx
console.log('hello ssafy!')

setTimeout(() => {
  console.log('1초 뒤에 실행됐지!')
}, 1000)

console.log('Bye ssafy!')

// Promise
const promise = new Promise((resolve, reject) => {
  
  setTimeout(() => {
    resolve('1초 뒤에 실행됐지!') // 1초 뒤에 하고 싶은 일!
  }, 1000)

})

promise 
  .then(value => {
    console.log('Hello ssafy!')
    console.log(value)
    console.log('Bye ssafy!')
  }) // resolve()가 실행됐을 때

// fetch 사용해보기
fetch('https://jsonplaceholder.typicode.com/todos/1') // requests.get()
  .then(res => {
    console.log(res)
  })
  .catch()

// axios -> html
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    axios.get('https://jsonplaceholder.typicode.com/todos/1')
      .then(res => {
        console.log(res.data.title)
      })
      .catch(err => {
        console.error(err)
        // 대응책
      })
  </script>
</body>
</html>
```

fetch : 내장함수

axios : 라이브러리 ( axios를 더 많이 사용 )

### Async & Await

- Promise를 더 쉽게 활용하기 위한 최신 문법 (syntactic sugar)
- 일반적인 함수에 async 키워드를 붙이면 비동기 함수가 된다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    /*
     1. async-await예시
     - syntatic sugar일 뿐 기능상에 차이는 없다.
     - 함수 앞에 반드시 async가 붙어있어야 한다.
    */

    async function fetchTodo() {
      const res = await axios.get('https://jsonplaceholder.typicode.com/todos/1') 
      console.log(res.data.title) // .then이 없어도 응답값이 잘 뜬다.
	    // 위에 코드가 끝나기 전엔 절대 밑에 코드가 실행되지 않는다.
		}

    fetchTodo()

		// 2-1 문제상황
		const requestUrls = [
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/2',
    'https://jsonplaceholder.typicode.com/todos/3'
    ]
    
    // requestUrls.forEach(url => {
    //   axios.get(url)
    //    .then(res => {
    //      console.log(res.data.title)
    //    })
    // })

		// 순서에 맞춰서 데이터를 받아오고 싶을 때
    async function fetchTodosInOrder(requestUrls) {
      const promises = []
      requestUrls.forEach(url => {
        const promise = axios.get(url)
        promises.push(promise)
      })

      Promise.all(promises)
        .then(responses => {
          console.log(responses)
        })
    }
    fetchTodosInOrder(requestUrls)

  </script>
</body>
</html>
```