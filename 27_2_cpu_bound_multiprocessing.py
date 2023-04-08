import time
from multiprocessing import current_process, Array, Manager, Process
import os

def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name

    print(f'Process ID: {process_id}, Process Name: {process_name}')

    total_list.append(sum(i * i for i in range(number)))

def main():
    numbers = [3000000 + x for x in range(30)]

    processes = []

    # 프로세스 공유 매니저
    manager = Manager()

    # 프로세스 공유
    total_list = manager.list()

    start_time = time.time()

    # 프로세스 생성 및 실행
    for i in numbers:
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list,))

        processes.append(t)

        t.start()

    for process in processes:
        process.join()

    result = sum(total_list)

    duration = time.time() - start_time
    print(f'result = {result}')
    print(f'Duration: {duration} seconds')

if __name__ == '__main__':
    main()

"""
Process ID: 8813, Process Name: 3000000
Process ID: 8814, Process Name: 3000001
Process ID: 8815, Process Name: 3000002
Process ID: 8818, Process Name: 3000003
Process ID: 8820, Process Name: 3000004
Process ID: 8822, Process Name: 3000005
Process ID: 8824, Process Name: 3000006
Process ID: 8826, Process Name: 3000007
Process ID: 8828, Process Name: 3000008
Process ID: 8830, Process Name: 3000009
Process ID: 8831, Process Name: 3000010
Process ID: 8832, Process Name: 3000011
Process ID: 8833, Process Name: 3000012
Process ID: 8834, Process Name: 3000013
Process ID: 8836, Process Name: 3000014
Process ID: 8837, Process Name: 3000015
Process ID: 8838, Process Name: 3000016
Process ID: 8839, Process Name: 3000017
Process ID: 8840, Process Name: 3000018
Process ID: 8841, Process Name: 3000019
Process ID: 8842, Process Name: 3000020
Process ID: 8843, Process Name: 3000021
Process ID: 8844, Process Name: 3000022
Process ID: 8845, Process Name: 3000023
Process ID: 8846, Process Name: 3000024
Process ID: 8847, Process Name: 3000025
Process ID: 8851, Process Name: 3000029
Process ID: 8849, Process Name: 3000027
Process ID: 8850, Process Name: 3000028
Process ID: 8848, Process Name: 3000026
result = 270003780024375058870
Duration: 1.1307413578033447 seconds
"""