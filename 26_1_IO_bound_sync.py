import requests
import time

def request_site(url, session):
    with session.get(url) as response:
        print(
            f"[Read Contents: {len(response.content)}, Status Code: {response.status_code}], from {url}"
              )

def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            request_site(url, session)

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
[Read Contents: 10782, Status Code: 200], from https://www.jython.org
[Read Contents: 274, Status Code: 200], from http://olympus.realpython.org/dice
[Read Contents: 67059, Status Code: 200], from https://realpython.com
[Read Contents: 10782, Status Code: 200], from https://www.jython.org
[Read Contents: 274, Status Code: 200], from http://olympus.realpython.org/dice
[Read Contents: 67059, Status Code: 200], from https://realpython.com
[Read Contents: 10782, Status Code: 200], from https://www.jython.org
[Read Contents: 274, Status Code: 200], from http://olympus.realpython.org/dice
[Read Contents: 67059, Status Code: 200], from https://realpython.com
Download 9 sites in 3.0931661128997803 seconds
"""