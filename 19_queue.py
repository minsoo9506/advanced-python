"""
- producer, consumer pattern
    - 멀티스레드 디자인 패턴의 정석
    - 서버측 프로그래밍의 핵심
- python event 객체
    1. Flag 초기값 = 0
    2. Set() -> 1, Clear() -> 0, Wait(1: return, 0: 대기), isSet() -> 현 flag
"""

import concurrent.futures
import logging
import queue
import random
import threading
import time

def producer(queue, event):
    """네트워크 대기 상태(I/O작업), 서버"""
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info(f"Producer got message={message}")
        queue.put(message)
        logging.info(f"Producer received event. Sending!")

def consumer(queue, event):
    """응답받고 소비, DB 저장"""
    while not event.is_set() or not queue.Empty():
        message = queue.get()
        logging.info(f"Consumer storing message={message}")
    logging.info(f"Consumer received event. Exit")


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)  # 운영하는 서비스에 따라 maxsize 설정
    event = threading.Event()  # 초기값 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        time.sleep(0.001)

        logging.info("main thread: set to event")

        # 종료
        event.set()
    