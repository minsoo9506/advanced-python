import multiprocessing
import requests
import time

# 함수 실행 할 떄 마다 객체 생성은 좋지 않음

session = None

def set_global_session():
    global session
    # 각 process에 없으면 session 만들어라
    if not session:
        session = requests.Session()

def request_site(url):
    print(f"session = {session}")
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"multiprocess name = {name}")
        print(
            f"[Read Contents: {len(response.content)}, Status Code: {response.status_code}], from {url}"
              )

def request_all_sites(urls):
    # initializer를 실행하고 작업진행
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)

def main():
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 3

    start_time = time.time()

    request_all_sites(urls)

    duration = time.time() - start_time

    print(f"Download {len(urls)} sites in {duration} seconds")

if __name__ == "__main__":
    main()


"""결과
session = <requests.sessions.Session object at 0x7f71ee155790>
session = <requests.sessions.Session object at 0x7f71ee155790>
session = <requests.sessions.Session object at 0x7f71ee155790>
session = <requests.sessions.Session object at 0x7f71ee155790>

multiprocess name = ForkPoolWorker-4
[Read Contents: 10782, Status Code: 200], from https://www.jython.org
multiprocess name = ForkPoolWorker-1
session = <requests.sessions.Session object at 0x7f71ee155790>
[Read Contents: 10782, Status Code: 200], from https://www.jython.org
session = <requests.sessions.Session object at 0x7f71ee155790>
multiprocess name = ForkPoolWorker-2
[Read Contents: 274, Status Code: 200], from http://olympus.realpython.org/dice
session = <requests.sessions.Session object at 0x7f71ee155790>
multiprocess name = ForkPoolWorker-2
[Read Contents: 10782, Status Code: 200], from https://www.jython.org
session = <requests.sessions.Session object at 0x7f71ee155790>
multiprocess name = ForkPoolWorker-3
[Read Contents: 67059, Status Code: 200], from https://realpython.com
session = <requests.sessions.Session object at 0x7f71ee155790>
multiprocess name = ForkPoolWorker-4
[Read Contents: 274, Status Code: 200], from http://olympus.realpython.org/dice
multiprocess name = ForkPoolWorker-2
[Read Contents: 274, Status Code: 200], from http://olympus.realpython.org/dice
multiprocess name = ForkPoolWorker-3
[Read Contents: 67059, Status Code: 200], from https://realpython.com
multiprocess name = ForkPoolWorker-1
[Read Contents: 67059, Status Code: 200], from https://realpython.com

Download 9 sites in 0.9865074157714844 seconds
"""