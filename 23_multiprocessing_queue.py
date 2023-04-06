"""
Queue, Pipe
"""

# 프로세스 통신 구현 Queue

from multiprocessing import Process, Queue, current_process
import time
import os

def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0

    for i in range(baseNum):
        sub_total += 1

    q.put(sub_total)
    print(f"Process ID: {process_id}, Process name: {process_name}, ID: {id}")
    print(f"Result = {sub_total}")

def main():
    parent_process_id = os.getpid()
    print(f"Parent process ID {parent_process_id}")

    processes = []

    # 시작 시간
    start_time = time.time()

    # Queue 선언
    q = Queue()

    for i in range(5):
        t = Process(name=str(i), target=worker, args=(i, 100000, q))

        processes.append(t)

        t.start()

    for process in processes:
        process.join()

    print(f"----{time.time() - start_time}----")

    # 종료 플래그
    q.put("exit")

    # queue를 통해서 메인프로세스로 값을 전달
    total = 0
    while True:
        tmp = q.get()
        if tmp == "exit":
            break
        else:
            total += tmp

    print(f"main-processing total count = {total}")
    print("main_process done")

if __name__ == "__main__":
    main()

"""결과
Parent process ID 11658
Process ID: 11659, Process name: 0, ID: 0
Result = 100000
Process ID: 11660, Process name: 1, ID: 1
Result = 100000
Process ID: 11661, Process name: 2, ID: 2
Result = 100000
Process ID: 11662, Process name: 3, ID: 3
Result = 100000
Process ID: 11663, Process name: 4, ID: 4
Result = 100000
----0.013628721237182617----
main-processing total count = 500000
main_process done
"""