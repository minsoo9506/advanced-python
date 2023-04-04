"""
- Semaphore vs Mutex
    - 둘 다 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용된다
    - Semaphore는 리소스에 대한 제한된 수의 동시 엑세스를 허용
    - Mutex는 단일 스레드만 리소스 엑세스를 허용
"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time

class FakeDataStore:
    def __init__(self) -> None:
        # thread들이 공유하는 변수 (data영역에 있음)
        self.value = 0

    def update(self, n):
        logging.info(f"Thread {n} start update!")

        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)  # 일부러 문제를 발생시키기 위해
        self.value = local_copy

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

"""
- 문제없이 진행된다면 결과 최종 결과값은 3이 나와야 한다.
    - 3개의 thread가 공유하는 self.value에 1을 더하기 때문이다.
- 하지만 실제로 돌려보면 1 또는 2가 나온다.
- 어떤 thread가 self.value = local_copy를 하기전에 (update전에) 
  다른 thread가 local_copy = self.value를 실행해버리기 때문이다.
"""
