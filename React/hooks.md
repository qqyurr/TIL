### route parameter

```react
<Route path="/workspace/:workspace" component={WorkSpace} />
```

:workspace -> route 파라미터, 자유롭게 값을 바꿀 수 있습니다. 

파라미터가 아니라 /workspace/sleact 이렇게 지정해준 주소면 파라미터를 사용한 주소보다 위에 위치해야 한다.



### SWR

```react
const { data: channelData } = useSWR<IChannel[]>(
    userData ? `http://localhost:3095/api/workspaces/${workspace}/channels` : null,
    fetcher,
  );
```

 login안해서 userData가 없으면 null 로 이동
 -> 내가 로그인했을 때만 요청할 수 있게 (SWR은 조건부 요청을 지원합니다. )

- SWR이 컴포넌트를 넘나들면서 전역 스토리지가 됩니다. 



### withCredentials

```react
  const onLogOut = useCallback(() => {
    axios
      .post('http://localhost:3095/api/users/logout', null, {
        withCredentials: true, 
      })
      .then(() => {
        mutate(false, false);
      });
  }, []);
```

axios 요청을 보낼 때 프론트와 백의 서버 주소가 다른 경우, 
쿠키를 서로 공유하려면 세번째 자리에 `withCredentials` 필수



### useParams

```react
const { workspace, channel } = useParams<{ workspace: string; channel: string }>();
```

 주소의 parameter를 useParams로 가져올 수 있다. 간단하게 주소에도 상태를 저장하고 useParams로 이를 이용할 수 있습니다. 