## Object Oriented Programming 객체 지향 프로그래밍

1. 상속 : 클래스 개념에서 상위 클래스(부모)로 부터 하위클래스(자식)이 유산을 물려받는 것과 같이 부모의 메소드나 변수를 사용할 수 있는 것을 말함
2. 다형성 : 같은 함수가 있을 때 매개변수에 따라 다른 역할을 할 수도 있다.
3. 캡슐화 : 데이터 은닉, 외부에서 쉽게 데이터를 접근할 수 없게, 데이터 구조와 데이터를 다루는 방법들을 한데다 묶는 것
4. 추상화 : 공통적인 속성이나 기능을 묶어서 이름을 붙이는 것

#### 객체지향 프로그래밍 5대 원칙 (SOLID)

> SRP(단일 책임 원칙)
> OCP(개방-폐쇄 원칙)
> LSP(리스코프 치환 원칙)
> ISP(인터페이스 분리 원칙)
> DIP(의존 역전 원칙)

 

\1. SRP(Single Responsiblity Principle) 단일 책임 원칙
\- 소프트웨어의 설계 부품(클래스, 함수 등)은 단 하나의 책임(기능)만을 가져야 한다. 

\2. Open-Closed Principle (개방-폐쇄 원칙)
\- 기존의 코드를 변경하지 않고(Closed) 기능을 수정하거나 추가할 수 있도록(Open) 설계해야 한다.
\- 자주 변경되는 기능이라면 수정하기 쉽게 설계

\3. Liskov Substitution Principle (리스코프 치환 원칙)
\- 자식 클래스는 부모클래스에서 가능한 행위를 수행할 수 있어야 한다. 부모 클래스와 자식 클래스 사이의 행위에는 일관성이 있어야 한다. 

\4. Dependency Inversion Principle (의존 역전 원칙)
\- 의존 관계를 맺을 때, 변화하기 쉬운것(구체적인것 ex. 구체화된 클래스) 보단 변화하기 어려운 것(추상적인 것 ex. 추상클래스, 인터페이스)에 의존해야 한다는 원칙이다.

\5. Interface Segregation Principle (인터페이스 분리 원칙)
\- 다른 기능들은 각각 독립된 인터페이스로 구현하여 서로에게 영향을 주지 않도록 설계해야 한다. 시스템의 내부 의존성을 약하게 하여 리팩토링, 수정, 재배포를 쉽게할 수 있도록 한다.

## 함수형 프로그래밍

\- 순수함수와 보조 함수의 조합을 통해 로직 내에 존재하는 조건문과 반복문을 제거하여 복잡성을 해결하고 변수의 사용을 억제하여 상태 변경을 피하려는 프로그래밍 패러다임이다.

\- 순수함수는 같은 입력이 주어지면 같은 출력을 반환해야하고, 부작용(side effect)이 없어야 한다.

\- 함수형 프로그래밍은 순수함수를 통해 side effect를 최대한 억제하여 오류를 피하고 프로그램의 안정성을 높이려는 노력의 한 방법

## OOP와 함수형 프로그래밍의 가장 큰 차이점

객체 지향 : 객체 안에 상태를 저장하고, 이 상태를 이용해서 메소드를 추가하고 상태 변화를 설정하고 조정하기 위해 다양한 기능을 사용한다.

함수형 프로그래밍 : 상태를 제어하는 것보다 상태를 저장하지 않고 없애는데 주력한다.

\- **객체지향**은 상태를 저장하는 필드와 그 필드들을 이용해 기능을 제공하는 메소드를 만들고 클래스를 만든다.

\- **함수형**은 몇몇 자료구조(list, map, set)등을 이용해 최적화된 동작을 만들어낸다.