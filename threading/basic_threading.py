import threading
import requests


def download_file(url):
    response = requests.get(url)
    print(f"Downloaded {url}")


urls = ["http://example.com/file1", "http://example.com/file2"]
threads = [threading.Thread(target=download_file, args=(url,)) for url in urls]

for thread in threads:
    print(thread.name)
    thread.start()  # activates and prompts a thread object to be run
for thread in threads:
    thread.join()  # delays a program’s flow of execution until the target thread has been completely read
