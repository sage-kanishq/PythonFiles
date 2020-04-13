# cook your dish here
import time
import concurrent.futures
start = time.perf_counter()

def doSomething(seconds):
    print(f"Start Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return f"Done Sleeping {seconds}"

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(doSomething,secs)
    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {finish-start:.2f}")