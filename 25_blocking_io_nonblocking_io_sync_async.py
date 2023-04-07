"""
blocking IO vs Non-blocking IO

blocking IO
- application이 kernel에 시스템 콜 요청 
    -> Kernel에서 IO 작업시작 (완료시까지 응답 대기)
    -> 그동안에 application은 대기 (block) = 다른 작업 수행 불가
    -> IO 작업 끝났다고 Kernel이 알려주면 다시 작업 수행 가능

Non-blocking IO
- application이 kernel에 시스템 콜 요청
    -> Kernel에서 IO 작업 시작 & 즉시 응답
    -> application 다른 작성 수행 가능 (non bloack)
    -> application이 주기적으로 시스템 콜 보내서 IO 작업 완료 여부 확인

Async vs Sync

Sync
- IO 작업 완료 여부에 대한 것을 app쪽에서 kernel로 콜 보내면서 확인
 
Async
- 반대로 kernel에서 완료되면 보내줌
"""

"""
그래서 예를 들어, Async Non-blocking IO는
- app에서 kernel에게 콜보내고 kernel을 IO작업시작
    -> app은 그동안 IO작업 신경쓰지 않고 다른 작업 수행
    -> kernel에서 IO작업이 끝나면 app에게 callback
"""