"""
sharing
- 프로세스는 리소소들을 독립적으로 쓰기때문에 나중에 결과를 합산해야하는 경우가 생긴다.
"""

from multiprocessing import Process, current_process, Value, Array
# from multiprocess import shared_memory: 도 사용하기 좋다
import os

# 프로세스 메모리 공유

# 실행함수
def generate_update_number(v):
    for _ in range(50):
        v.value += 1
    print(f"{current_process().name} data: {v.value}")

def main():
    parent_process_id = os.getpid()
    print(f"Parent process ID {parent_process_id}")

    processes = []

    # 변수의 type도 알려줘야함 i는 int를 의미
    # 리스트 사용하고 싶은 경우: Array("i", range(10))
    share_value = Value("i", 0)  

    # 예상되는 결과는 share_value=450
    for _ in range(1, 10):
        p = Process(target=generate_update_number, args=(share_value,))
        processes.append(p)

        p.start()

    for p in processes:
        p.join()

    print(f"result share_value = {share_value.value}")

if __name__ == "__main__":
    main()

"""결과
processing_sharing.py
Parent process ID 12110
Process-1 data: 50
Process-2 data: 100
Process-3 data: 150
Process-4 data: 200
Process-5 data: 250
Process-6 data: 300
Process-7 data: 350
Process-8 data: 400
Process-9 data: 450
result share_value = 450
"""