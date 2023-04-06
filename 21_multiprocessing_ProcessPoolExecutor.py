"""
ProcessPoolExecutor
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

URLS = [
    "http://www.daum.net",
    "http://www.cnn.com/",
    "http://naver.com"
]

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()
    
def main():
    with ProcessPoolExecutor(max_workers=3) as executor:
        # future 로드
        # future가 key, url이 value
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

        for future in as_completed(future_to_url):
            url = future_to_url[future]

            try:
                data = future.result()
            except Exception as exc:
                print(f"{url} generated an exception: {exc}")
            else:
                print(f"{url} page is {len(data)} bytes")


if __name__ == "__main__":
    main()

""" 결과
http://naver.com page is 209252 bytes
http://www.cnn.com/ page is 1150047 bytes
http://www.daum.net page is 777996 bytes
"""