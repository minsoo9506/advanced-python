import time

def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sum(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    return result

def main():
    numbers = [3000000 + x for x in range(30)]

    start_time = time.time()

    total = find_sum(numbers)
    result = sum(total)

    duration = time.time() - start_time
    print(f'result = {result}')
    print(f'Duration: {duration} seconds')

if __name__ == '__main__':
    main()

"""
result = 270003780024375058870
Duration: 5.205019235610962 seconds
"""