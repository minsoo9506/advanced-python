"""
(1) 프로세스
    - 운영체제 -> 할당 받는 자원 단위 (실행 중인 프로그램)
    - CPU동작 시간, 주소공간(독립적)
    - Code, Data, Stack, Heap -> 각 프로세스마다 독립적
    - 최소 1개의 메인스레드 보유
    - 파이프, 파일, 소켓등을 사용해서 프로세스간 통신 -> Context Switching 으로 cost가 높음

(2) 스레드
    - 프로세스 내에 최소 실행 흐름 단위
    - 프로세스 자원 사용
    - Stack만 별도 할당 나머지는 공유 (Code, Data, Heap)
    - 메모리 공유 (변수 공유)
    - 한 스레드의 결과가 다른 스레드에 영향 끼침
    - 동기화 문제 발생 가능 (디버깅 어려움)

(3) 멀티 스레드
    - 한 개의 단일 어플리케이션 -> 여러 스레드로 구성 후 작업 처리
    - 시스템 자원 소모 감소 (효율성), 처리량 증가 (Cost 감소)
    - 통신 부담 감소, 디버깅 어려움, 단일 프로세스에는 효과 미약, 자원 공유 문제 (교착상태)

(4) 멀티 프로세스
    - 한 개의 단일 어플리케이션 -> 여러 프로세스로 구성 후 작업 처리
    - 한 개의 프로세스 문제 발생 시 다른 프로세스 영향 없음
    - 캐시 체인지, Cost 비용 높음 (오버헤드), 복잡한 통신 방식 사용
"""

import logging
import threading
import time

# thread 함수
def thread_func(name):
    logging.info(f"sub-Thread {name}: start!")
    time.sleep(3)
    logging.info(f"sub-Thread {name}: end!")

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("main-Thread: before creating thread")

    x = threading.Thread(target=thread_func, args=('example',))

    logging.info("main-Thread: before running thread")

    # 서브 스레드 실행
    x.start()

    # join명령어 사용하면 sub thread가 끝나야 뒤 명령어 진행
    # x.join()

    logging.info("main-Thread: wait thread to be finished")

    logging.info("main-Thread: all done")

"""결과
22:50:00: main-Thread: before creating thread
22:50:00: main-Thread: before running thread
22:50:00: sub-Thread example: start!
22:50:00: main-Thread: wait thread to be finished
22:50:00: main-Thread: all done
22:50:03: sub-Thread example: end!
"""