"""
Naming
"""

from multiprocessing import Process, current_process
import os
import time

def square(n):
    time.sleep(1)
    process_id = os.getpid()
    process_name = current_process().name

    result = n * n
    print(f"Process Id: {process_id}, Process Name: {process_name}")
    print(f"Result of {n} square: {result}")

if __name__ == "__main__":
    parent_process_id = os.getpid()  # process id 가져오기
    print(f"Parent process Id {parent_process_id}")

    processes = []

    for i in range(1, 10):
        # 생성
        t = Process(name=str(i), target=square, args=(i,))  # process 생성

        # 배열에 넣기
        processes.append(t)

        # 시작
        t.start()

    for process in processes:
        process.join()

    print("process done")

"""결과
Parent process Id 12344
Process Id: 12345, Process Name: 1
Result of 1 square: 1
Process Id: 12346, Process Name: 2
Result of 2 square: 4
Process Id: 12347, Process Name: 3
Result of 3 square: 9
Process Id: 12348, Process Name: 4
Result of 4 square: 16
Process Id: 12349, Process Name: 5
Result of 5 square: 25
Process Id: 12350, Process Name: 6
Process Id: 12351, Process Name: 7
Result of 6 square: 36
Result of 7 square: 49
Process Id: 12352, Process Name: 8
Result of 8 square: 64
Process Id: 12353, Process Name: 9
Result of 9 square: 81
process done
"""