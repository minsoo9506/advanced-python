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