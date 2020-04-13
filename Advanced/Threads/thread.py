import time
import concurrent.futures

def doSomething(seconds):
    print(f"Start Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return f"Done Sleeping {seconds}"
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(doSomething,secs)
    for result in results:
        print(result)


finish = time.perf_counter()
print(f"Finished in {finish-start:.2f}")