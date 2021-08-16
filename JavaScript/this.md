# this

객체지향 프로그래밍 : 객체는 상태를 나타내는 `프로퍼티`와 동작을 나타내는 `메서드`를 하나의 논리적 단위로 묶은 복합적 자료구조

동작을 나타내는 메서드는 자신이 속한 객체의 상태, 즉 프로퍼티를 참조하고 변경할 수 있어야 한다. 이때 메서드가 자신이 속한 객체의 프로퍼티를 참조하려면 자신이 속한 객체를 가리키는 식별자를 참조할 수 있어야 합니다. 

생성자 함수를 정의하는 시점에는 아직 인스턴스를 생성하기 이전입니다. 

그렇기 때문에 생성자 함수가 생성할 인스턴스를 가리키는 식별자를 알 수 없다.

따라서 자신이 속한 객체, 또는 자신이 생성할 인스턴스를 가리키는 특수한 식별자가 필요하다. 이를 위해 자바스크립트는 this라는 특수한 식별자를 제공합니다. 

## this 키워드

"*this는 자신이 속한 객체, 또는 자신이 생성할 인스턴스를 가리키는 자기 참조 변수"*

this를 통해 자신이 속한 객체, 또는 자신이 생성할 인스턴스의 프로퍼티나 메서드를 참조할 수 있다. 

this가 가리키는 값, 즉 this 바인딩은 함수 호출 방식에 의해 동적으로 결정됩니다.

### 객체 리터럴과 생성자 함수의 예제

```jsx
// 객체 리터럴
const circle = {
	radius: 5,
	getDiameter(){
		// this는 메서드를 호출한 객체를 가리킨다.
		return 2*this.radius;
	}
};

console.log(circle.getDiameter()); //10
```

객체 리터럴에서의 메서드 내부에서의 this는 메서드를 호출한 객체, 즉 circle을 가리킨다.

### 생성자 함수 내부의 this

```jsx
// 생성자 함수
function Circle(radius){
	// this는 생성자 함수가 생성할 인스턴스를 가리킨다.
	this.radius = radius;
}

Circle.protoype.getDiameter = function () {
	// this는 생성자 함수가 생성할 인스턴스를 가리킨다.
	return 2 * this.radius;
};

const circle = new Circle(5);
console.log(circle.getDiameter()); // 10
```

생성자 함수 내부의 this는 생성자 함수가 생성할 인스턴스를 가리킨다. 

- 자바스크립트의 this는 함수가 호출되는 방식에 따라 this에 바인딩될 값, 즉 this 바인딩이 동적으로 결정된다. strict mode 역시 this 바인딩에 영향을 줍니다.

### this는 코드 어디에서든 참조 가능!

```jsx
// this는 어디에서든지 참조가능
// 전역에서 this는 전역 객체 window를 가리킨다.
console.log(this);

function square(number){
	// 일반 함수 내부에서 this는 전역 객체 window를 가리킨다.
	console.log(this); // window
	return number * number;
}
square(2) //4

const person = {
	name: 'Lee',
	getName(){
		// 메서드 내부에서 this는 메서드를 호출한 객체를 가리킨다.
		console.log(this); // {name: "Lee", getName: f}
		return this.name; 
	}
}
console.log(person.getName()); // Lee

function Person(name){
	this.name = name;
	// 생성자 함수 내부에서 this는 생성자 함수가 생성할 인스턴스를 가리킨다.
	console.log(this); // Person {name : "Lee"}
}

const me = new Person('Lee');
```

# [생성자 함수](https://ko.javascript.info/constructor-new#ref-1183)

생성자 함수(constructor function)와 일반 함수에 기술적인 차이는 없습니다. 다만 생성자 함수는 아래 두 관례를 따릅니다.

1. 함수 이름의 첫 글자는 대문자로 시작합니다.
2. 반드시 `'new'` 연산자를 붙여 실행합니다

this는 객체의 프로퍼티나 메서드를 참조하기 위한 자기 참조 변수이므로 일반적으로 객체의 메서드 내부 또는 생성자 함수 내부에서만 의미가 있다. 따라서 strict mode가 적용된 일반 함수 내부의 this에는 undefined가 바인딩된다. 일반함수 내부에서 this를 사용할 필요가 없기 때문이닷.

## 함수 호출 방식과 this 바인딩

this 바인딩은 함수 호출 방식, 즉 함수가 어떻게 호출되었는지에 따라 동적으로 결정된다. 

- 렉시컬 스코프와 this 바인딩은 결정 시기가 다르다.
    - 함수의 상위 스코프를 결정하는 방식인 렉시컬 스코프는 함수 정의가 평가되어 함수 객체가 생성되는 시점에 상위 스코프를 결정한다. 하지만 this 바인딩은 함수 호출 시점에 결정된다.

함수를 호출하는 방식

1. 일반 함수 호출
2. 메서드 호출
3. 생성자 함수 호출
4. Function.prototype.apply/call/bind 메서드에 의한 간접 호출

```jsx
const foo = function(){
	console.dir(this);
}

// 1. 일반 함수 호출
foo(); // window

// 2. 메서드 호출
// foo 함수를 프로퍼티 값으로 할당하여 호출,
// foo 함수 내부의 this는 메서드를 호출한 객체 obj를 가리킨다.
const obj = { foo };
obj.foo(); // obj

// 3. 생성자 함수 호출
// foo 함수를 new 연산자와 함께 생성자 함수로 호출
// foo 함수 내부의 this는 생성자 함수가 생성한 인스턴스를 가리킨다.
new foo(); // foo {}

// 4. Function.prototype/apply/call/bind 메서드에 의한 간접 호출
// foo 함수내부의 this는 인수에 의해 결정된다.
const bar = { name: 'bar' };
foo.call(bar); //bar
foo.apply(bar); //bar
foo.bind(bar)(); // bar
```

### 일반함수 호출

```jsx
function foo() {
	console.log(this); //window
	function bar() {
		console.log(this); // window
	}
	bar();
}
foo();
```

- 기본적으로 this에는 전역 객체가 바인딩된다.

    객체를 생성하지 않는 일반함수에서는 this는 의미가 없다. strict mode에선 undefined가 바인딩된다.

- 콜백함수 내부의 this에서 전역 객체가 바인딩 된다. 어떠한 함수라도 일반함수로 호출되면 this에 전역 객체가 바인딩됩니다.

```jsx
var value = 1;

const obj = {
	value: 100,
	foo() {
		console.log(this) // {value:100, foo:f}
		setTimeout(function(){
			console.log(this); // window
			console.log(this.value); // 1
		},100)
	}
}

obj.foo();
```

- 일반 함수로 호출된 모든 함수 (중첩 함수, 콜백 함수 포함) 내부의 this에는 전역 객체가 바인딩됩니다.

### 메서드 내부의 중첩함수나 콜백함수의 this 바인딩을 메서드의 this 바인딩과 일치시키기 위한 방법

```jsx
var value = 1;

const obj = {
	value: 100,
	foo() {
		console.log(this) // {value:100, foo:f}
		const that = this; // this 바인딩(obj)를 that에 할당한다.
		// 콜백함수 내부에서 this 대신 that을 참조한다. 
		setTimeout(function(){
			console.log(that.value) // 100
		},100)
	}
}

obj.foo();
```

```jsx
var value = 1;

const obj = {
	value: 100,
	foo() {
		// 콜백함수에 명시적으로 this를 바인딩한다.
		setTimeout(function(){
			console.log(this.value) // 100
		}.bind(this),100)
	}
}

obj.foo();
```

```jsx
var value = 1;

const obj = {
	value: 100,
	foo() {
		// 화살표 함수 내부의 this는 상위 스코프 this를 가리킨다.
		setTimeout(()=> console.log(this.value),100); // 100
	}
}

obj.foo();
```