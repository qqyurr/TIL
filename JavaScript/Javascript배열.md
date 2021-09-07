# Javascript 배열

- 자바스크립트에 배열이라는 타입은 존재하지 않는다. 배열은 객체 타입이다.

  ```javascript
  typeof arr // -> object
  ```

- 배열은 배열 리터럴, Array 생성자 함수, Array.of, Array.from 메서드로 생성할 수 있다. 배열의 생성자 함수는 Array이며, 배열의 프로토타입 객체는 Array.prototype이다. Array.prototype은 배열을 위한 빌트인 메서드를 제공한다. 

```javascript
const arr = [1,2,3];

arr.constructor === Array // -> true
Object.getPrototypeOf(arr) === Array.prototype // -> true
```

- 배열은 객체지만 일반 객체와 구별되는 독특한 특징이 있다.
  - 값의 순서(index), length 프로퍼티
- length 프로퍼티 값은 요소의 개수, 즉 배열의 길이를 바탕으로 결정되지만 임의의 숫자값을 명시적으로 할당할 수도 있다. 

```javascript
const arr = [1,2,3,4,5];

// 현재 length 프로퍼티 값이 5보다 작은 숫자 값 3을 length 프로퍼티에 할당
arr.length = 3;

// 배열의 길이가 5에서 3으로 줄어든다.
console.log(arr); // [1,2,3]
```

- 희소배열(배열의 요소가 연속적으로 위치하지 않고 일부가 비어있는 배열)

```javascript
// 희소 배열
const sparse = [,2,,4];

// 희소 배열의 length 프로퍼티 값은 요소의 개수와 일치하지 않는다.
console.log(sparse.length); //4
console.log(sparse) // [empty, 2, empty, 4]

// 배열 sparse에는 인덱스가 0, 2인 요소가 존재하지 않는다.
console.log(Object.getOwnPropertyDescriptors(sparse));

/*
{
	'1':{value:2, writable: true, enumerable:true, configurable:true},
 	'3':{value:4, writable: true, enumerable:true, configurable:true},
 	length:{value: 4, writable: ture, enumerable: false, configurable: false}
 }
*/
```

- 배열 요소 추가

```javascript
const arr = [];

// 배열 요소 추가
arr[0] = 1;
arr['1'] = 2;

// 프로퍼티 추가
arr['foo'] = 3;
arr.bar = 4;
arr[1.1] = 5;
arr[-1] = 6;
console.log(arr); // [1,2,foo:3, bar:4, '1.1':5, '-1':6]

// 프로퍼티는 length에 영향을 주지 않는다.
console.log(arr.length) // 2
```

- 배열 요소 삭제

``` javascript
const arr = [1,2,3];

delete arr[1]; 
console.log(arr); // [1,empty,3] -> 희소배열이 된다.
console.log(arr.length); // 3
```

희소배열을 만들지 않기 위해 delete 연산자는 사용하지 않는 것이 좋다.

Array.prototype.splice 메서드를 사용한다.

```javascript
const arr = [1,2,3];

arr.splice(1,1);
console.log(arr) // [1,3]
console.log(arr.length) // 2
```

