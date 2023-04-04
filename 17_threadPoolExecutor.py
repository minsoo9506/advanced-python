"""
ThreadPoolExecutor
- 여러개의 thread를 쉽게 사용하도록 해주는 파이썬 내장 패키지
- concurrent.futures
- {}PoolExecutor
"""

import logging
from concurrent.futures import ThreadPoolExecutor

def task(name):
    logging.info(f"sub-Thread {name}: start!")

    result = 0
    for i in range(1, 10001):
        result = result + i
    logging.info(f"sub-Thread {name}: result = {result}!")

    return result

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    logging.info("main-Thread: before creating and running thread")

    ### 실행방법1 ###
    # # max_workers: The maximum number of threads that can be used to execute the given calls.
    # excutor = ThreadPoolExecutor(max_workers=2)
    # task1 = excutor.submit(task, ('first'))
    # task2 = excutor.submit(task, ('second'))

    # # 결과값이 있을 경우
    # print(task1.result())
    # print(task2.result())

    ### 실행방법2 ###
    with ThreadPoolExecutor(max_workers=2) as executor:
        tasks = executor.map(task, ['first', 'second'])

        print(list(tasks))