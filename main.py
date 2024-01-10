import requests
import threading
from queue import Queue

def threader():
    while True:
        worker = q.get()

        make_request(worker)

        q.task_done()
def make_request(subdomain):
    try:
        response = requests.get(subdomain)
        if response.status_code == 200:
            print("Found subdomain -----> " + subdomain)
    except requests.exceptions.RequestException as e:
        pass
num_threads = 10

q = Queue()

for x in range(num_threads):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

target_input = "google.com"
with open("subdomainlist.txt", "r") as sub_domainlist:
    for word in sub_domainlist:
        word = word.strip()
        url = f"http://{word}.{target_input}"
        q.put(url)

q.join()
