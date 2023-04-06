"""
daemon thread
- 백그라운드에 실행
- 메인스레드 종료시 즉시 종료
"""

import logging
import threading
import time

# thread 함수
def thread_func(name, second):
    logging.info(f"sub-Thread {name}: start!")
    for i in range(1, second + 1):
        print(f'{i}초...')
        time.sleep(1)
    logging.info(f"sub-Thread {name}: end!")

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("main-Thread: before creating thread")

    # main thread가 done하면 x,y가 바로 종료됨
    x = threading.Thread(target=thread_func, args=('example1', 5), daemon=True)
    y = threading.Thread(target=thread_func, args=('example2', 3), daemon=True)

    logging.info("main-Thread: before running thread")

    # 서브 스레드 실행
    x.start()
    y.start()

    logging.info("main-Thread: wait thread to be finished")

    logging.info("main-Thread: all done")

"""결과
22:49:45: main-Thread: before creating thread
22:49:45: main-Thread: before running thread
22:49:45: sub-Thread example1: start!
1초...
22:49:45: sub-Thread example2: start!
1초...
22:49:45: main-Thread: wait thread to be finished
22:49:45: main-Thread: all done
"""