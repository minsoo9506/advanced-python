"""
- Semaphore vs Mutex
    - 둘 다 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용된다
    - Semaphore는 리소스에 대한 제한된 수의 동시 엑세스를 허용
    - Mutex는 단일 스레드만 리소스 엑세스를 허용
"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class FakeDataStore:
    def __init__(self) -> None:
        # thread들이 공유하는 변수 (data영역에 있음)
        self.value = 0
        self._lock = threading.Lock()

    def update(self, n):
        logging.info(f"Thread {n} start update!")

        # thread synchronization 필요

        # (방법1)
        # # Lock 획득 
        # self._lock.acquire()
        # logging.info(f"thread {n} has lock")

        # local_copy = self.value
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy

        # # Lock 반환 
        # self._lock.release()
        # logging.info(f"thread {n} release lock")

        # (방법2)
        ## with문 이용
        with self._lock:
            logging.info(f"thread {n} has lock")

            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

            logging.info(f"thread {n} release lock")

        logging.info(f"Thread {n} end update!")


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    store = FakeDataStore()

    logging.info(f"Test update. Starting valid is {store.value}")

    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['first', 'second', 'third']:
            executor.submit(store.update, n)

    logging.info(f"Testing update. Ending value is {store.value}")