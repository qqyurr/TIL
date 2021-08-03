# Memoization

기존 수행한 연산의 결과값을 따로 저장해두고, 동일한 입력이 들어오면 재활용하는 프로그래밍 기법. 적절히 사용하면 중복 연산을 피해서 성능을 최적화할 수 있다.

# useMemo

`useMemo` 함수는 2개의 인자를 받습니다. 첫번째는 결과값을 생성해주는 팩토리 함수

두번째는 Dependency

```jsx
const memoizedValue = useMemo(()=>
	computedExpensiveValue(a,b),[a,b]);
```

useMemo는 Dependency의 값이 변경되었을 경우에만 Memoization된 값만 다시 계산합니다.

Dependency안의 값이 바뀌지 않았다면, 이전에 연산한 값을 재사용하게 됩니다.

이는 모든 렌더링 시의 고비용 계산을 방지해줍니다. `useMemo` 로 전달된 함수는 렌더링 중에 실행됩니다.

useMemo를 적절하게 사용한다면 성능 최적화를 가져올 수 있지만, 컴포넌트의 복잡도가 올라가서 코드의 가독성이 떨어지고 유지보수성도 떨어지게 됩니다.

또한 useMemo가 적용된 레퍼런스는 재활용을 위해서 가비지 컬렉션에서 제외되기 때문에 메모리를 더 쓰게 됩니다.

# useCallback

useCallback은 `함수 메모이제이션` 을 하는 리액트 훅 입니다.

리액트는 컴포넌트가 렌더링 될 때마다 해당하는 함수가 새롭게 생성됩니다.

```jsx
const memoizedCallback = useCallback(
  () => {
    doSomething(a, b);
  },
  [a, b],
);
```

- a,b의 값이 바뀌면 새로운 함수가 생성
- 바뀌지 않는다면 다음 렌더링 때 함수 재사용

useCallback()을 사용하면 해당 컴포넌트가 렌더링되더라도 함수가 의존하는 dependency 값들이 바뀌지 않으면 기존 함수를 계속해서 반환합니다.

# React.memo()

React는 먼저 컴포넌트를 렌더링하고, 렌더된 결과와 비교하여 DOM 업데이트를 결정합니다.

컴포넌트가 `React.memo()`로 래핑될 때, React는 컴포넌트를 렌더링하고 결과를 Memoizing 합니다. 그리고 다음 렌더링이 일어날 때 props가 같다면 React는 Memoizing된 내용을 재사용합니다.

React.memo()를 사용하면 좋은 상황

1. 같은 props로 렌더링이 자주 일어나는 컴포넌트
2. 무겁고 비용이 큰 연산이 있는 경우