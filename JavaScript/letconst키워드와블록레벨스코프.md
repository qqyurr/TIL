# let, const 키워드와 블록 레벨 스코프

### var

- 변수 중복 선언 가능

```javascript
var x = 1;
var y = 1;

var x = 100;
var y;

console.log(x); //100
console.log(y); //1
```

> `var y;` 와 같은 초기화문의 유무에 따라 다르게 동작합니다. 초기화문이 있는 변수 선언문은 자바스크립트 엔진에 의해 var 키워드가 없는 것처럼 동작합니다. 초기화무이 없는 변수 선언문은 무시됩니다. 

- 함수 레벨 스코프

```javascript
var x = 1;

if (true) {
    var x = 10;
}

console.log(x); // 10
```

> 함수 외부에서 var 키워드로 선언한 변수는 코드 블록 내에서 선언해도 전역변수가 됩니다. 

- 변수 호이스팅

```javascript
console.log(foo); // undefined

foo = 123;

console.log(foo) // 123

var foo; // 변수 선언
```

> 변수 선언은 런타임 이전에 자바스크립트 엔진에 의해 암묵적으로 실행된다.
>
> 그렇기에 첫째줄에서 foo를 출력했을 때 끌어올려지는 것처럼 foo가 undefined로 출력됩니다.
>
> 그 이후 foo가 123으로 할당된 뒤에 foo를 출력하면 123이 출력됩니다. 



### let 

- 변수 중복 선언 금지

```javascript
let bar = 123;
let bar = 456; // SyntaxError : Identifier 'bar' has already been declared.
```

> 중복 선언 시 문법 에러 발생

- 블록 레벨 스코프

```javascript
let foo = 1;
{
    let foo = 2;
    let bar = 3;
}
console.log(foo); // 1
console.log(bar); // ReferenceError: bar is not defined
```

> 전역으로 선언한 변수와 지역으로 선언한 변수는 이름이 같아도 별개의 변수가 됩니다. 지역에서 선언한 변수를 전역에서 출력하려하면 ReferenceError가 발생합니다. 

- 변수 호이스팅

```javascript
console.log(foo); // ReferenceError: foo is not defined
let foo;
```

> 호이스팅이 발생하지 않는 것처럼 보인다.
>
> var의 경우 선언단계와 초기화단계가 한번에 진행됩니다. 자바스크립트 엔진에 의해 선언됨과 동시에 초기화 단계에서 undefined가 됩니다. let은 선언단계와 초기화단계가 분리되어 진행됩니다. 자바스크립트 엔진에 의해 선언되지만 초기화 단계가 실행되기 이전에 변수에 접근하려 하면 Referrence Error가 발생합니다. 스코프의 시작 지점부터 초기화 시작 지점까지 변수를 참조할 수 없는 구간을 `일시적 사각지대` 라고 부릅니다.



### const

- 선언과 초기화

```javascript
const foo = 1;
```

> const로 선언한 변수는 반드시 동시에 초기화해야 합니다.

```javascript
{
    console.log(foo); // ReferrenceError
    const foo = 1;
    console.log(foo);// 1
}

console.log(foo); // ReferenceError
```

> 블록 레벨 스코프를 가지고 호이스팅이 실행되지 않는 것처럼 보입니다.

- 재할당 금지

```javascript
const foo = 1;
foo = 2; // TypeError
```

- 상수

```javascript
const TAX_RATE = 0.1

let preTaxPrice = 100;

let afterTaxPrice = preTaxPrice + (preTaxPrice*TAX_RATE);

console.log(afterTaxPrice); 
```

> 상수는 재할 당이 금지된 변수를 말합니다. 일반적으로는 대문자로 선언하고, 여러 단어로 이뤄진 경우 `_` 로 구분하여 표현합니다.

- const 키워드와 객체

> const 키워드로 선언된 변수에 객체를 할당한 경우 값을 변경할 수 있습니다. 새로운 값을 재할당하는 것은 불가능하지만 프로퍼티 동적 생성, 삭제, 프로퍼티 값의 변경을 통해 객체를 변경하는 것은 가능합니다. 

