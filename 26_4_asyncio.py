"""
asyncio 
"""

import time
import asyncio

# 비동기 함수 async 붙이기
async def process_async():
    start = time.time()

    # 비동기 함수안에 비동기 함수 부르면 await
    await asyncio.wait([
        exe_calculate_async('work1', 3),
        exe_calculate_async('work2', 2),
        exe_calculate_async('work3', 1)
    ])

    end = time.time()

    print(f">>> time: {end - start}")

async def exe_calculate_async(name, n):
    for i in range(1, n + 1):
        print(f"{name} -> {i} of {n} is calculated")
        await asyncio.sleep(1)
    print(f"{name} is done")


if __name__ == '__main__':
    # 비동기 함수 실행을 위해 run
    asyncio.run(process_async())

"""결과
work1 -> 1 of 3 is calculated
work3 -> 1 of 1 is calculated
work2 -> 1 of 2 is calculated
work1 -> 2 of 3 is calculated
work3 is done
work2 -> 2 of 2 is calculated
work1 -> 3 of 3 is calculated
work2 is done
work1 is done
>>> time: 3.004235029220581
"""