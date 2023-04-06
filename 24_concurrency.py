"""
Concurrency, CPU bound vs IO bound
"""

"""
Concurrency
- cpu 사용 극대화를 위해 병렬화의 단점을 소프트웨어레벨에서 해결하기 위한 방법
- 싱글코어에 멀티스레드 패턴으로 작업을 처리
- 동시 작업에 있어서 일정량 처리 후 다음 직업으로 넘기는 방식
- 제어권을 주고 받으면서 작업 처리, 병렬적이지는 않지만 유사한 방식
"""

"""
Concurrency vs Parallelism
- Concurrency
    - 논리적 동시 실행, 싱글&멀티 코어에서 실행 가능, 한 개의 작업 공유 처리
- Parallelism
    - 물리적 동시 실행, 멀티코어에서 구현 가능, 주로 별개의 작업 처리
"""