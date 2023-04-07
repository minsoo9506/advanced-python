import concurrent.futures
import threading
import requests
import time

# 각 스레드에 생성되는 객체
# 즉 공유할 필요가 없는 경우
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def request_site(url):
    session = get_session()
    with session.get(url) as response:
        print(
            f"[Read Contents: {len(response.content)}, Status Code: {response.status_code}], from {url}"
              )

def request_all_sites(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)

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


"""결과: threading를 사용(multithread)하니까 시간이 단축됨 (sync보다)
[Read Contents: 10782, Status Code: 200], from https://www.jython.org
[Read Contents: 10782, Status Code: 200], from https://www.jython.org
[Read Contents: 67059, Status Code: 200], from https://realpython.com
[Read Contents: 10782, Status Code: 200], from https://www.jython.org
[Read Contents: 274, Status Code: 200], from http://olympus.realpython.org/dice
[Read Contents: 274, Status Code: 200], from http://olympus.realpython.org/dice
[Read Contents: 67059, Status Code: 200], from https://realpython.com
[Read Contents: 67059, Status Code: 200], from https://realpython.com
[Read Contents: 274, Status Code: 200], from http://olympus.realpython.org/dice
Download 9 sites in 2.1458334922790527 seconds
"""